import pymysql
db = pymysql.connect("localhost","testuser","test123","sakila",3306)
cursor = db.cursor()
sql = "SELECT * FROM TEST_TABLE"
try:
    cursor.execute(sql)
    resultset = cursor.fetchall()
    for row in resultset:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]      
        print("%s %s, %d, %s, %d" %(fname, lname, age, sex, income))

    print("The records fetched successfully!")
except:
    print("The records were not fetched!")
db.close()
