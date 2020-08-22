import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1234',
    database='testdb',
)
mycursor=mydb.cursor()
sqlformula='INSERT INTO students(name,age) VALUES(%s,%s)'
'''
student1=('Maher',24)
mycursor.execute(sqlformula,student1)
'''
students=[('sunny',21),
('Rahi',21),
('Armin',20),
('Bappu',25)]
mycursor.executemany(sqlformula,students)
mydb.commit()
