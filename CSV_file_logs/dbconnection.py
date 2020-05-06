import pymysql

def getcursorconnection():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='227pankaj27', db='filesrecord')
    cursor = conn.cursor()
    return conn, cursor
