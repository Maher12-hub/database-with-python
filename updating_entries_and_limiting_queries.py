import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='testdb'
)
mycursor=mydb.cursor()
#sql="UPDATE students SET age=24 WHERE name='Bappu'"
#sql="INSERT INTO students (name,age) VALUES(%s,%s)"
#students=[('Anha',6),('Doha',4)]
#mycursor.executemany(sql,students)
mycursor.execute("SELECT * FROM students LIMIT 4 OFFSET 4")
myresult=mycursor.fetchall()
for result in myresult:
    print(result)