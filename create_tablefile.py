import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="root",database="employees")
print(conn)
cur = conn.cursor()
sql = "create table emp_data(emp_id int ,emp_name varchar(20))"
sql = "insert into emp_data values(1,'rohi')"
try:
    cur.execute(sql)
except Exception as e:
    print(e)
else:
    print("table create")
    print("inserted")
finally:
    conn.close()

