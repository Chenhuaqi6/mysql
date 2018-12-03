import pymysql

#创建数据库连接对象
db = pymysql.connect("localhost","root","123456","db5",charset = "utf8")


#利用数据库连接对象创建１个游标对象
cursor = db.cursor()


#执行ｓｑｌ命令
cursor.execute("insert into t2(name,score) values('王维',88)")

#提交到数据库执行
db.commit()
print("ok")

#关闭游标对象
cursor.close()

#断开与数据库连接
db.close()