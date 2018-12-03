import pymysql

db = pymysql.connect(host="localhost",user = "chenhuaqi",password = "726316",database = "db5",charset = "utf8")


cur = db.cursor()
#cur.execute("use db5")
sel = "select * from t2"
cur.execute(sel)

one = cur.fetchone()
print(one)
print("*"*30)

many = cur.fetchmany(2)
for x in many:
    print(x)

print("*"*30)

All = cur.fetchall()
for a in All:
    print(a)

db.commit()
cur.close()
db.close()