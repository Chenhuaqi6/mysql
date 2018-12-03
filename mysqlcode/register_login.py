from mysqlpython import Mysqlpython

#加密模块
from hashlib import sha1

menu = """1.注册
2.登录
q.退出
请选择(1/2/q):"""
#到数据库user表中去查
sqlh = Mysqlpython("db5")
while 1:
    choice = input(menu)
    if choice.strip()== "1":

        # 先让用户输入注册的用户名
        uname = input("请输入用户名:")
        sele = "select username from user where username = %s"
        r = sqlh.all(sele,[uname])

        if r:
            print("用户名已存在")
            continue
        else:
            pwd1 = input("请输入密码:")
            pwd2 = input("请再次输入密码:")
            #密码一致,注册成功
            if pwd1 == pwd2:
                #对密码进行加密,存入数据库
                s = sha1()  #创建sha1加密对象
                s.update(pwd1.encode("utf8")) #不能对字符串加密  要把字符串转为字节流 
                pwd = s.hexdigest()  #返回十六进制加密结果

                ins = "insert into user values(%s,%s)"
                sqlh.zhixing(ins,[uname,pwd])
                print("注册成功")
            else:
                print("密码不一致")
    elif choice.strip() == "2":
        #登录功能
        #接收用户输入的用户名和密码
        uname = input("请输入用户名:")
        pwd = input("请输入密码:")


        #到数据库中查询
        sel = "select password from user where username = %s"

        result = sqlh.all(sel,[uname])
        # print(result)

        # (('cb08cc50ecce578cfd9bc2fef3ef84a4ff686062',),)
        s = sha1()
        s.update(pwd.encode("utf8"))
        pwd2 = s.hexdigest()
        if len(result) == 0:
            print("用户名不存在")
        elif result[0][0] == pwd2:
            print("登录成功")
            break
        else:
            print("密码错误")
    elif choice.strip() == "q":
        print("感谢使用")
        break



