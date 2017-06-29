#coding:utf-8
from app.db import DBmain

class User(object):
    
    def __init__(self):
        self.db = DBmain.DBModel()
        pass
    
    def isExistUser(self,param):
        sql = " SELECT * FROM user WHERE id = %s ";
        return self.db.exeOneMySQL(sql,param)
    
    def insertUserGetInertId(self,param):
        sql = " INSERT INTO user (nick_name,user_name,puid,add_time) values(%s,%s,%s,%s) "
        data = self.db.insertMySQLById(sql,param)
        return data["id"]
    
    def updateUserInfo(self,param):
        sql = " UPDATE user set nick_name=%s,user_name=%s,puid=%s,update_time=%s WHERE id=%s "
        return self.db.updateMySQL(sql,param)
    
    def getUserInfoByUserName(self,param):
        sql = " SELECT * FROM user WHERE user_name = %s ";
        return self.db.exeOneMySQL(sql,param)
    
    def getToalUserInfo(self):
        sql = " SELECT * FROM user  ";
        return self.db.exeAllMySQL(sql)
    