import pymysql

db = pymysql.connect("localhost","testuser","test123","sakila",3306)

cursor = db.cursor()

sql = "SELECT VERSION()"

cursor.execute(sql)

data = cursor.fetchone()

print("Database version : %s" % data)

db.close()
