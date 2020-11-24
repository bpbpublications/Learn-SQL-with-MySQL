import pymysql

db = pymysql.connect("localhost","testuser","test123","sakila",3306)
cursor = db.cursor()

sql1 = """INSERT INTO TEST_TABLE (FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES('Ashwin', 'Pajankar', 32, 'M', 1000)"""

sql2 = """INSERT INTO TEST_TABLE (FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES('Thor', 'Odinson', 35, 'M', 2000)"""

sql3 = """INSERT INTO TEST_TABLE (FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES('Tony', 'Stark', 40, 'M', 40000)"""

sql4 = """INSERT INTO TEST_TABLE (FIRST_NAME,
    LAST_NAME, AGE, SEX, INCOME)
    VALUES('Jane', 'Foster', 32, 'F', 3000)"""

try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    db.commit()
    print("The records inserted successfully!")
except:
    db.rollback()
    print("The records were not inserted!")

db.close()
