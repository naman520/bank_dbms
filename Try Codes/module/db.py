import mysql.connector as sql

def db():
    conn = sql.connect(host = 'localhost',user = 'root', passwd='123456',database = 'BANK_DBMS')
    cur = conn.cursor()
    query = cur.execute('SELECT * FROM customer_login')
    results = cur.fetchall()
    for i in results:
        print(i)

db()