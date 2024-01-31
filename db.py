from flask import Flask
import pymysql
app=Flask(__name__)
def get_conn():
    return pymysql.connect(
        host='127.0.0.1',
        user='boot',
        password='123456',
        database='pymysql',
        charset='utf8'
    )

#query database
def query_data(sql):
    conn=get_conn()
    try:
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(f'error:{e}')
    finally:
        conn.close()

#insert or update database
def insert_data(sql):
    conn=get_conn()
    try:
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()

if __name__=='__main__':
    app.run()

