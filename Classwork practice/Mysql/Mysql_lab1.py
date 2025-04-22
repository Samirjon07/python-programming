import mysql.connector
from mysql.connector import Error

connector=mysql.connector.connect(
    host="localhost",
    password="Samirjon07",
    user="root",
    database="siut"
)
if connector.is_connected():
    print("Connected")
    
mycursor=connector.cursor()

mycursor.execute("SELECT * FROM students")
myresult=mycursor.fetchall()
print(myresult)