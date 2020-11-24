import pymysql

db = pymysql.connect("localhost","testuser","test123","sakila",3306)
cursor = db.cursor()

sql = "UPDATE TEST_TABLE SET INCOME = INCOME + 500 WHERE SEX = '%c'" % ('F')

try:
    cursor.execute(sql)

    db.commit()

    print("The records updated successfully!")
except:
    db.rollback()
    print("The records were not updated!")

db.close()
