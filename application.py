from flask import Flask, render_template, request, flash, g
from flask import redirect, url_for, session, jsonify
import sys
import pymysql
import mysql.connector
from database import DBhandler
import re
from collections import Counter



application = Flask(__name__)
application.secret_key = 'your_secret_key'

#db = DBhandler()



db = pymysql.connect(host='127.0.0.1', user='root', password='0322', db='skintreedb', charset='utf8')
cursor = db.cursor()




def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0


def calculate_jaccard_similarity(user_input, ingredients_list):
    # 텍스트에서 이차원 리스트 추출
    # findall->string 전체에서 패턴과 일치하는 것을 모두 찾아 list로 반환
    inner_lists = re.findall(r'\[.*?\]', ingredients_list)
    #print(inner_lists)
    # 각 내부 리스트를 파이썬 리스트로 변환
    text_to_lists = [eval(lst) for lst in inner_lists]

    #print(text_to_lists)


    user_inner_lists = re.findall(r'\[.*?\]', user_input)
    #print(inner_lists)
    # 각 내부 리스트를 파이썬 리스트로 변환
    user_text_to_lists = [eval(lst) for lst in user_inner_lists]

    combined_ingList = set()
    for sublist in text_to_lists:
        for item in sublist:  # 수정: 사용자 입력도 리스트의 리스트가 아니므로 중첩 반복문 사용
            combined_ingList.add(item.strip())
            #print(item.strip())

    # 대괄호를 제거하고 하나의 리스트로 만들기
    combined_userInput = set()
    for sublist in user_text_to_lists:
        for item in sublist:  # 수정: 사용자 입력도 리스트의 리스트가 아니므로 중첩 반복문 사용
            combined_userInput.add(item.strip())  # 수정: add 함수로 각 항목 추가
    #combined_ingList 와 combined_userInput에 각 성분이 하나씩 들어가있음
    # print("user_input_set:", combined_userInput)
    # print("ingredients_list_set:", combined_ingList, "\n")

    # 자카드 유사도 계산
    return jaccard_similarity(combined_userInput, combined_ingList)

def random_recommendation(user_category, user_input):
    # 사용자의 카테고리와 일치하는 제품을 찾아야 함
    cursor.execute("SELECT productID, productIngredients FROM product WHERE categoryID = %s", (user_category,))
    products = cursor.fetchall()

    highest_similarity = 0
    most_similar_productID = None

    # 각 제품의 유사도 계산 및 비교
    for productID, productIngredients in products:
        similarity = calculate_jaccard_similarity(user_input, productIngredients)
        print("productID:", productID, "유사도:", similarity)  # 각 유사도 출력
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_productID = productID

    if highest_similarity > 0.6:
        print("Most similar productID:", most_similar_productID)
    else:
        print("No products with similarity over 0.6. No recommendation.\n")



def find_most_similar_user(user_input):
    user_similarities = []

    # useringredients 테이블에서 모든 행 가져오기
    cursor.execute("SELECT userID, ingredientsList FROM userIngredients")
    result = cursor.fetchall()

    # 각 행의 유사도 계산 및 비교
    for userID, ingredientsList in result:
        
        similarity = calculate_jaccard_similarity(user_input, ingredientsList)
        user_similarities.append((userID, similarity))
        print("userID:", userID, "유사도:", similarity)  # 각 유사도 출력
        #print(f"userID의 유저인풋{user_input}")

    # 유사도에 따라 내림차순 정렬
    user_similarities.sort(key=lambda x: x[1], reverse=True)

    # 상위 3명의 userID 추출(자신은 유사도1이니까 그다음부터)
    top_3_users = [userID for userID, sim in user_similarities[1:4] if sim > 0.3]

    #top_3_users = top_3_users[1:]

    # 반환된 top_3_users에 따라 조건부로 find_users_recommend_products 함수 호출
    if top_3_users:
        print("Top3 most similar userIDs:", top_3_users)
        product_names = find_users_recommend_products(top_3_users, cursor, user_category)
        return product_names
    else:
        print("No users with similarity over 0.6. Recommending random product.\n")
        random_recommendation(user_category, user_input)
        return None



def find_users_recommend_products(top_3_users, cursor, user_category):
    cursor.execute("SELECT productID FROM user WHERE userID = %s", (user_id_result,))
    mycosmetics = cursor.fetchall()  # 요청한 유저의 productID를 가져옴 (이미 존재하는 화장품은 추천에서 제외하기위해)
    # 각 사용자에 대해 처리
    product_names=[]
    for userID in top_3_users:
        # fitness가 "good"이고 해당 사용자의 모든 productID를 찾음
        cursor.execute("SELECT productID FROM user WHERE userID = %s AND fitness = 'Good'", (userID,))
        results = cursor.fetchall()  # 모든 행을 가져옴

        #product_names = []  # 추천 제품의 이름을 저장할 리스트
        
        for result in results:
            if result not in mycosmetics: #추천유저의 pdID가 사용자의 pdID랑 겹치지 않을때
                productID = result[0]  # 튜플의 첫 번째 요소가 productID
                #print(f"유저추천제품ID: {userID}의 {productID}")
                # productID를 사용하여 해당 제품의 productName과 categoryID를 가져옴
                cursor.execute("SELECT translated_productName, categoryID FROM product WHERE productID = %s", (productID,))
                product_result = cursor.fetchone()
                #print(f"product_result[0]: {product_result[0]}")
                #print(f"product_result[1]: {product_result[1]}")
                #print(f"유저 카테고리: {user_category}")
                #print(f"{type(int(user_category))} {type(product_result[1])}")
                if (product_result and product_result[1] == int(user_category)):
                    #print(f"카테고리 일치하는 화장품 존재함")
                    productName = product_result[0]  # productName은 튜플의 첫 번째 요소
                    product_names.append(productName)  # productName을 리스트에 추가
                    print(f"유저추천제품NAME: {userID}의 {productName}")
                # print(f"유저추천제품NAMELIST:{product_names}")

        # 최대 3개까지의 추천 제품 출력
    if product_names:
        #중복 제거 (애초에 더하기 안되게 하거나 빈도수 활용하는데 사용하기)
        #product_names=set(product_names)
        #product_names=list(product_names)
        count_product_items = Counter(product_names)
        print(f"빈도수순 정렬 {count_product_items}")
        Top_3_product_items=count_product_items.most_common(n=3)
        Top_3_product_names = [item[0] for item in Top_3_product_items]
        print(f"UserID {userID}: Recommended products: {', '.join(product_names[:])}")
        return Top_3_product_names[:]
    else:
        print(f"UserID {userID}: No recommended product found for user_category {user_category}")
        #return None



def get_initial_data():
    # 데이터베이스 연결
    db = pymysql.connect(host='127.0.0.1', user='root', password='0322', db='skintreedb', charset='utf8')
    
    # 데이터에 접근
    cursor = db.cursor()

    # SQL query 실행
    cursor.execute("SELECT * FROM product")
    product = cursor.fetchall()

    cursor.execute("SELECT * FROM user")
    user = cursor.fetchall()

    cursor.execute("SELECT * FROM userIngredients")
    userIngredients = cursor.fetchall()  

    # Database 닫기
    cursor.close()
    db.close()

    return product, user, userIngredients


@application.route("/")
def hello():
    product, user, userIngredients = get_initial_data()
    return render_template("Home.html", product=product, user=user)

@application.route("/submit_email", methods=['POST'])
def submit_email():
    email = request.form.get('email')

    if not email: # 이메일 미입력시 처리
        product, user = get_initial_data()
        return render_template("Home.html", product=product, user=user)
    
    session['user_email'] = email  # 입력된 이메일을 세션에 저장
    return redirect(url_for('Insert'))


@application.route("/Insert")
def Insert():
    product, user, userIngredients = get_initial_data()
    user_email = session.get('user_email', None)
    db = pymysql.connect(host='127.0.0.1', user='root', password='0322', db='skintreedb', charset='utf8')
    cursor = db.cursor()

    query = """
    SELECT user.productID, product.translated_productName, user.fitness, product.productID
    FROM user
    JOIN product ON user.productID = product.productID
    WHERE user.email = %s
    """

    cursor.execute(query, (user_email,))
    result = cursor.fetchall()

    cursor.close()

    return render_template("Insert_product.html",user_email=user_email, current_page='Insert_product.html',products=result, product=product, user=user)

def update_user_ingredient():
    email = session.get('user_email')  # 세션에서 이메일 주소 가져오기

    if email:
        db = DBhandler()

        # 특정 이메일을 가진 사용자의 userID 검색
        query = "SELECT userID FROM user WHERE email = %s"
        user_id = db.execute_query(query, (email,))
        
        if user_id:
            user_id = user_id[0][0]  # 튜플 형태로 반환되므로 첫 번째 요소만 사용
            #print(f"{user_id}")
            # 해당 사용자가 구매한 productID를 사용하여 productIngredients 검색
            query = "SELECT productIngredients FROM product WHERE productID IN (SELECT productID FROM user WHERE email = %s)"
            product_ingredients = db.execute_query(query, (email,))
            ingredients_list=[]
            # productIngredients를 하나의 리스트로 합치기
            ingredients_list = ', '.join([row[0] for row in product_ingredients]) if product_ingredients else ''
            # 위에서 얻은 ingredientsList를 userIngredient 테이블에 저장
            # 이미 동일한 userID가 존재하는지 확인하는 쿼리
            query = "SELECT COUNT(*) FROM userIngredients WHERE userID = %s"
            count = db.execute_query(query, (user_id,))[0][0]

            if count > 0:
                # 이미 동일한 userID가 존재하면 업데이트
                query = "UPDATE userIngredients SET ingredientsList = %s WHERE userID = %s"
                db.execute_query(query, (ingredients_list, user_id))
            else:
                # 존재하지 않으면 새로운 행 삽입
                query = "INSERT INTO userIngredients (userID, ingredientsList) VALUES (%s, %s)"
                db.execute_query(query, (user_id, ingredients_list))
            db.commit()
            db.close_connection()

            return "User ingredient updated successfully."
        else:
            db.close_connection()
            return "User not found."
    else:
        return "No email found in session."



@application.route("/insert_product", methods=["POST"])
def insert_product():

    #db = pymysql.connect(host='127.0.0.1', user='root', password='0322', db='skintreedb', charset='utf8')
    #cursor = db.cursor()

    # 클라이언트로부터 데이터 받기
    user_email = session.get('user_email', None)
    email = session.get('user_email', None)
    product_name = request.form.get("product_name")
    fitness = request.form.get("fitness")
    print(f"제품명 확인 {product_name}")
    print(f"적합 확인 {fitness}")

    # user 테이블에서 이메일로부터 userID 가져오기
    user_id_query = "SELECT userID FROM user WHERE email = %s"
    cursor.execute(user_id_query, (user_email,))
    user_id_result = cursor.fetchone()

    if user_id_result:
        user_id = user_id_result[0]
    else:
        # 새로운 사용자이므로 새로운 userID 생성
        max_user_id_query = "SELECT MAX(userID) FROM user"
        cursor.execute(max_user_id_query)
        max_user_id_result = cursor.fetchone()
        if max_user_id_result[0]:
            user_id = max_user_id_result[0] + 1
        else:
            user_id = 1    
        
    # product 테이블에서 productName으로부터 productID 가져오기
    product_id_query = "SELECT productID FROM product WHERE translated_productName = %s"
    cursor.execute(product_id_query, (product_name,))
    product_id_result = cursor.fetchone()
    print(f"제품명 아이디 확인 {product_id_result}")
    if product_id_result:
        product_id = product_id_result[0]

        print(f"제품명 아이디 확인2 {product_id_result[0]}")     
        # 중복 여부 확인
        check_query = "SELECT COUNT(*) FROM user WHERE userID = %s AND productID = %s"
        cursor.execute(check_query, (user_id, product_id))
        count_result = cursor.fetchone()

        if count_result[0] == 0:
            # user table에 데이터 입력하기
            insert_query = "INSERT INTO user (userID, email, productID, fitness) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (user_id, user_email, product_id, fitness))
            db.commit()
            update_user_ingredient()
            db.commit()

            return redirect(url_for('Insert'))
        else:
            update_query = "UPDATE user SET fitness = %s WHERE userID = %s AND productID = %s"
            cursor.execute(update_query, (fitness, user_id, product_id))
            
            db.commit()
            update_user_ingredient()
            db.commit()
            return redirect(url_for('Insert',current_page=request.path))
    else:
        return redirect(url_for('Insert'))
    
    
    

@application.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    # 데이터베이스 연결
    db = pymysql.connect(host='127.0.0.1', user='root', password='0322', db='skintreedb', charset='utf8')
    cursor = db.cursor()

    # DELETE 쿼리 실행
    delete_query = "DELETE FROM user WHERE productID = %s"
    cursor.execute(delete_query, (product_id,))

    
    # 변경 사항 커밋
    db.commit()
    update_user_ingredient()
    db.commit()
    # Database 닫기
    cursor.close()
    db.close()


    # 다시 Insert 페이지로 리다이렉트 또는 필요한 페이지로 리다이렉트
    return redirect(url_for('Insert'))




@application.route('/Select_category')
def Select_category():

    user_email = session.get('user_email')

    # 사용자의 데이터가 user 테이블에 있는지 확인
    db = pymysql.connect(host='127.0.0.1', user='root', password='0322', db='skintreedb', charset='utf8')
    cursor = db.cursor()

    try:
        query = "SELECT COUNT(*) FROM user WHERE email = %s"
        cursor.execute(query, (user_email,))
        user_exists = cursor.fetchone()[0]

        if user_exists:
            # 사용자의 데이터가 user 테이블에 있으면 Select_category 페이지로 이동
            return render_template("Select_category.html",current_page='Select_category.html')
        else:
            flash('제품을 한 개 이상 입력해주세요.')
            return redirect(url_for('Insert'))
    except Exception as e:
        # 에러 처리
        print(f"An error occurred: {str(e)}")
    finally:
        # Database 닫기
        cursor.close()
        db.close()
    

@application.route('/Recommend')
def Recommend():
    global user_category
    global user_id_result
    category = request.args.get('category','')
    # user ingredient 리스트 만드는 함수 실행 

    #update_user_ingredient()
    
    #useringredients 불러오기 (추후 따로 함수로 만들기)
    user_email = session.get('user_email', None)
    email = session.get('user_email')
    user_category=category
    
    if user_email:
        db = pymysql.connect(host='127.0.0.1', user='root', password='0322', db='skintreedb', charset='utf8')
        cursor = db.cursor()

        # 이메일을 사용하여 userID 검색
        user_id_query = "SELECT userID FROM user WHERE email = %s"
        cursor.execute(user_id_query, (email,))
        user_id_result = cursor.fetchone()

        if user_id_result:
            user_id = user_id_result[0]

            # userID를 사용하여 userIngredients의 ingredientsList 검색
            ingredients_query = "SELECT ingredientsList FROM userIngredients WHERE userID = %s"
            cursor.execute(ingredients_query, (user_id,))
            ingredients_result = cursor.fetchone()

            if ingredients_result:
                ingredients_list = ingredients_result[0]
            
                #ingredients_list = [ingredient.strip("[]").replace("'", "").split(", ") for ingredient in ingredients_list]
              
                user_input = ingredients_list
                print(f"유저인풋타입{type(user_input)}")
                #예전 버전
                #user_input = [ingredient.strip("[]").replace("'", "").split(", ") for ingredient in user_input]
                #user_input = '[' + user_input + ']'
                #print(f"유저인풋타입2{type(user_input)}")
                #user_input 타입은 str 임
                print(f"유저아이디{user_id}")
                print(f"선택한 카테고리: {category}")
                #print(f"최종입력버전{user_input}")
                most_similar_userID = find_most_similar_user(user_input)
                #find_users_recommend_products(most_similar_userID, cursor)
                if most_similar_userID:
                    return render_template('Recommend.html', current_page='Recommend.html', most_similar_userID=most_similar_userID,user_email=user_email)
                else:
                    return render_template('Recommend.html', current_page='Recommend.html', user_email=user_email)
                
            else:
                return "User ingredients not found."
        else:
            return "User ID not found."
    else:
        return "User email not found in session."


    # 머신러닝 함수 실행하기 (database나 백엔드단에서 작성)

    # category 변수에 저장되어있음 이 아래 실행안되는 부분임
    print(f"선택한 카테고리 {category}")
    return render_template('Recommend.html', current_page='Recommend.html')



@application.route('/Restart')
def Restart():
    return render_template('Restart.html', current_page='Restart.html')


@application.route("/back")
def back():
    current_page = request.args.get('current_page', '')
    print(f"Moving from {current_page} to...")
    if current_page == 'Insert_product.html':
        return redirect(url_for('hello'))
    elif current_page == 'Select_category.html':
        return redirect(url_for('Insert'))
    elif current_page == 'Recommend.html':
        return redirect(url_for('Select_category'))
    elif current_page == 'Restart.html':
        return redirect(url_for('Recommend'))
    else:
        return redirect(url_for('hello'))
    

@application.route("/next")
def next():
    current_page = request.args.get('current_page', '')
    print(f"Moving from {current_page} to...")
    if current_page == 'Insert_product.html':
        return redirect(url_for('Select_category'))
    elif current_page == 'Select_category.html':
        return redirect(url_for('Select_category'))
    elif current_page == 'Recommend.html':
        return redirect(url_for('Restart'))
    else:
        return redirect(url_for('hello'))


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3000, debug=True)
