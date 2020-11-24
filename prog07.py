import pymysql
db = pymysql.connect("localhost","testuser","test123","sakila",3306)
cursor = db.cursor()
sql = "DROP TABLE TEST_TABLE"
try:
    cursor.execute(sql)
    print("The table dropped successfully!")
except:
    print("The object does not exist!")
db.close()
