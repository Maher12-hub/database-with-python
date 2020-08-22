import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='testdb',
)
mycursor=mydb.cursor()
#sql="DELETE FROM students WHERE name='sunny'"
#sql="DROP TABLE students "
sql="DROP TABLE IF EXISTS students"
mycursor.execute(sql)
mydb.commit()