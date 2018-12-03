from mysqlpython import Mysqlpython


a=Mysqlpython("db5")
# a.zhixing("insert into t2(name,score) values('奥特曼',100)")
# a.zhixing("update t2 set score = 99.99")
print(a.many("select * from t2",4))
print(a.all("select * from t2",))