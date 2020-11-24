import pymysql

db = pymysql.connect("localhost","testuser","test123","sakila",3306)

cursor = db.cursor()

try:
    sql = """CREATE TABLE TEST_TABLE (
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20) NOT NULL,
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT)"""

    cursor.execute(sql)
    print("The table created successfully!")
except:
    print("The table already exists in the database!")

db.close()
