import mysql.connector
from mysql.connector import Error

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Samirjon07",
    database="python"
)

if conn.is_connected():
    print("Connection established")

mycursor = conn.cursor()
mycursor.execute("INSERT INTO grades (id) VALUES('15')")
conn.commit()

mycursor.execute("SELECT * FROM grades")    


myresult = mycursor.fetchall()
print(myresult)