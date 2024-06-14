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

    def close_cursor(self):
        self.cursor.close() 

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


   