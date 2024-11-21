import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="#Thuvan9787",database="python_database")
if con:
    print("connected")
else:
    print("not connected")
