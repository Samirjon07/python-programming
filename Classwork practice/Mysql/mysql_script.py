import mysql.connector
from mysql.connector import Error

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="siut"
)

if conn.is_connected():
    print("Connection established")

mycursor = conn.cursor()
mycursor.execute("SELECT * FROM course")
myresult = mycursor.fetchall()
print(myresult)
