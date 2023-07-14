import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="root")
print(conn)
cur = conn.cursor()
sql = "create database employees"
cur.execute(sql)