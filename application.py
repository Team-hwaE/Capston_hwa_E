from flask import Flask, render_template, request
from flask import redirect, url_for, session, jsonify
import sys
import pymysql
import mysql.connector


application = Flask(__name__)
application.secret_key = 'your_secret_key'


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

    # 다시 Insert 페이지로 리다이렉트 또는 필요한 페이지로 리다이렉트
    return redirect(url_for('Insert'))


@application.route('/Select_category')
def Select_category():
    return render_template('Select_category.html', current_page='Select_category.html')


@application.route('/Recommend')
def Recommend():
    return render_template('Recommend.html', current_page='Recommend.html')


@application.route('/Restart')
def Restart():
    return render_template('Restart.html', current_page='Restart.html')


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
