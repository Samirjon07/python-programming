import mysql.connector
from mysql.connector import Error

connect=mysql.connector.connect(
    host='localhost',
    password='Samirjon07',
    user='root',
    database='siut'
)

if connect.is_connected():
    print("Connection established")
    
    
mycursor=connect.cursor()
mycursor.execute("INSERT INTO students(std_id) VALUES(19)")
connect.commit()

mycursor.execute("SELECT * FROM students")
myresult=mycursor.fetchall()
print(myresult)