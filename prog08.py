import pymysql
db = pymysql.connect("localhost", "testuser", "test123", "world",3306)
import pandas as pd
df1 = pd.read_sql('select * from country', db)
print(df1)
