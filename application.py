from flask import Flask, render_template, request
from flask import redirect, url_for, session, jsonify
import sys
application = Flask(__name__)


@application.route("/")
def hello():
    return render_template("Home.html")


@application.route("/Insert")
def Insert():
    return render_template("Insert_product.html", current_page='Insert_product.html')


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
