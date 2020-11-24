import pymysql

db = pymysql.connect("localhost","testuser","test123","sakila",3306)
cursor = db.cursor()

sql = "DELETE FROM TEST_TABLE"

try:
    cursor.execute(sql)

    db.commit()

    print("The records deleted successfully!")
except:
    db.rollback()
    print("The records were not deleted!")

db.close()
