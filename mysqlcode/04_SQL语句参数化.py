import pymysql

db = pymysql.connect(host = "localhost",user = "chenhuaqi",password = "726316",charset = "utf8")


cursor = db.cursor()

cursor.execute("use db5")

name = input("请输入学生姓名: ")

score = input("请输入学生成绩: ")

try:
    ins = "insert into t2(name,score) values(%s,%s)"

    #execute 中的第二个参数一定要为列表
    cursor.execute(ins,[name,score])
    db.commit()
    print("添加成功")
except:
    db.rollback()
    print("添加失败")
cursor.close()
db.close()