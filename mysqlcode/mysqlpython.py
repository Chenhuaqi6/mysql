import pymysql


class Mysqlpython:
    def __init__(self,database,host = "localhost",user = "chenhuaqi",password = "726316",charset = "utf8",port = 3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port

    
    def open(self):
        self.db = pymysql.connect(database=self.database,host = self.host,user = self.user,password = self.password,charset = self.charset,port = self.port)
        self.cur = self.db.cursor()
    def close(self):
        self.cur.close()
        self.db.close()

    def zhixing(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        self.db.commit()

        self.close()
    
    def all(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        result = self.cur.fetchall()
        self.close()
        return result
    
    def many(self,sql,n,L=[]):
        self.open()
        self.cur.execute(sql,L)
        result = self.cur.fetchmany(n)
        self.close()
        return result
















