import pymysql

def getcursorconnection():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='yourpassword', db='usa_cars')
    cursor = conn.cursor()
    return conn, cursor
