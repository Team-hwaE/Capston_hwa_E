from flask import Flask, render_template, request
from flask import redirect, url_for, session, jsonify
import sys
import pymysql
import mysql.connector
from database import DBhandler

application = Flask(__name__)
application.secret_key = 'your_secret_key'

db = DBhandler()

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

  

    # Database 닫기
    cursor.close()

    return product, user


@application.route("/")
def hello():
    product, user = get_initial_data()
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
    product, user = get_initial_data()
    user_email = session.get('user_email', None)
    db = pymysql.connect(host='127.0.0.1', user='root', password='0322', db='skintreedb', charset='utf8')
    cursor = db.cursor()

    query = """
    SELECT user.productID, product.productName, user.fitness, product.productID
    FROM user
    JOIN product ON user.productID = product.productID
    WHERE user.email = %s
    """

    cursor.execute(query, (user_email,))
    result = cursor.fetchall()

    cursor.close()

    return render_template("Insert_product.html",user_email=user_email, current_page='Insert_product.html',products=result, product=product, user=user)


@application.route("/insert_product", methods=["POST"])
def insert_product():

    db = pymysql.connect(host='127.0.0.1', user='root', password='0322', db='skintreedb', charset='utf8')
    cursor = db.cursor()

    # 클라이언트로부터 데이터 받기
    user_email = session.get('user_email', None)
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
    product_id_query = "SELECT productID FROM product WHERE productName = %s"
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

            return redirect(url_for('Insert'))
        else:
            update_query = "UPDATE user SET fitness = %s WHERE userID = %s AND productID = %s"
            cursor.execute(update_query, (fitness, user_id, product_id))
            db.commit()

            return redirect(url_for('Insert',current_page=request.path))
    else:
        return "Product not found."
    
    
    

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

    # Database 닫기
    cursor.close()
    db.close()

    # 다시 Insert 페이지로 리다이렉트 또는 필요한 페이지로 리다이렉트
    return redirect(url_for('Insert'))


@application.route('/Select_category')
def Select_category():
    return render_template('Select_category.html', current_page='Select_category.html')


def update_user_ingredient():
    email = session.get('user_email')  # 세션에서 이메일 주소 가져오기

    if email:
        db = DBhandler()

        # 특정 이메일을 가진 사용자의 userID 검색
        query = "SELECT userID FROM user WHERE email = %s"
        user_id = db.execute_query(query, (email,))
        
        if user_id:
            user_id = user_id[0][0]  # 튜플 형태로 반환되므로 첫 번째 요소만 사용
            print(f"{user_id}")
            # 해당 사용자가 구매한 productID를 사용하여 productIngredients 검색
            query = "SELECT productIngredients FROM product WHERE productID IN (SELECT productID FROM user WHERE email = %s)"
            product_ingredients = db.execute_query(query, (email,))

            # productIngredients를 하나의 리스트로 합치기
            ingredients_list = ', '.join([row[0] for row in product_ingredients])
            print(f"합친 성분리스트 {ingredients_list}")
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


@application.route('/Recommend')
def Recommend():
    category = request.args.get('category','')
    # user ingredient 리스트 만드는 함수 실행 
    update_user_ingredient()
    
    # 머신러닝 함수 실행하기 (database나 백엔드단에서 작성)

    # category 변수에 저장되어있음
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
        return redirect(url_for('Recommend'))
    elif current_page == 'Recommend.html':
        return redirect(url_for('Restart'))
    else:
        return redirect(url_for('hello'))


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8000, debug=True)
