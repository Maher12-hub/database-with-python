import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='testdb',
)
mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM students')
myresult=mycursor.fetchall()
for row in myresult:
    print(row)