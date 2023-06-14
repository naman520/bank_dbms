import mysql.connector as sql

conn=sql.connect(host='localhost',user='root',passwd='123456')
cur = conn.cursor()

#creating database
#db = cur.execute('CREATE DATABASE BANK_DBMS')
db = cur.execute('USE BANK_DBMS')

# ADMIN TABLE
#table = cur.execute('CREATE TABLE ADMIN(USERNAME STRING(30),PASSWORD STRING(8))')

# INSERTING VALUE 1
tb_val = cur.execute('INSERT INTO ADMIN (USERNAME STRING,PASSWORD STRING) VALUES("username@012","admin012")')