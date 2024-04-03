""" 다른 프로젝트에서 참고하려고 가져온 코드임 
@application.route("/submit_item_post", methods=['POST'])
def reg_item_submit_post():
    ##image_file = request.files["file"]
    ##image_file.save("static/images/{}".format(image_file.filename))
    data = request.form
    ##sessionid = session.get('id')
    DB.insert_item(data['name'], data, image_file.filename, sessionid)

    return render_template("submit_item_result.html", data=data,
                           img_path="static/images/{}".format(image_file.filename))


def insert_item(self, name, data, img_path, sessionid):
        item_info = {
            "price": data["price"],
            "addr": data['addr'],
            "status": data['status'],
            "send": data['send'],
            "keyword": data["keyword"],
            "explain": data["explain"],
            "img_path": img_path,
            "seller": sessionid,
            "openkakao": data['openkakao'],
            "confirm":0
        }
        self.db.child("item").child(name).set(item_info)
        print(data, img_path)
        return True

"""

import json
import pymysql
import mysql.connector

class DBhandler:
    def __init__(self):
        self.connection = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="0322",
            database="skintreedb"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.fetchall()
    

    def commit(self):
        self.connection.commit()
        

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


   