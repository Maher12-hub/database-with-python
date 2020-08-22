import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='testdb'
)
mycursor=mydb.cursor()
'''
#mycursor.execute('CREATE DATABASE testdb')
mycursor.execute('SHOW DATABASES')
for db in mycursor:
    print(db)
'''
mycursor.execute('CREATE TABLE students (name VARCHAR(255), age INTEGER(15))')
mycursor.execute('SHOW TABLES')
for db in mycursor:
    print(db)