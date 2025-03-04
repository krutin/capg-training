
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cmr_batch1"
)

cursor = conn.cursor()

# cursor.execute("insert into employees(name,email,address) values('rishi','rishi@gmail.com','asdf')")

cursor.execute("SELECT * FROM employees")


result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
conn.close()