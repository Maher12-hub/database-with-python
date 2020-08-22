import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='testdb',
)
mycursor=mydb.cursor()
#sql='SELECT * FROM students WHERE age=21'
#sql="SELECT * FROM students WHERE name LIKE 'Ma%'"
sql="SELECT * FROM students WHERE name LIKE '%ah%'"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for result in myresult:
    print(result)