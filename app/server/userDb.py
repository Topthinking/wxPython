# coding:utf-8
from app.db import DBmain


class User(object):

    def __init__(self):
        self.db = DBmain.DBModel()
        pass

    def isExistUser(self, param):
        sql = ' SELECT * FROM user WHERE id = %s ';
        return self.db.exeOneMySQL(sql, param)

    def insertUserGetInertId(self, param):
        sql = " INSERT INTO user (nick_name,user_name,puid,add_time) values(%s,%s,%s,%s) "
        data = self.db.insertMySQLById(sql, param)
        return data["id"]

    def updateUserInfo(self, param):
        sql = " UPDATE user set nick_name=%s,user_name=%s,puid=%s,update_time=%s WHERE id=%s "
        return self.db.updateMySQL(sql, param)

    def getUserInfoByUserName(self, param):
        sql = " SELECT * FROM user WHERE user_name = %s ";
        return self.db.exeOneMySQL(sql, param)

    def getToalUserInfo(self):
        sql = " SELECT * FROM user ";
        return self.db.exeAllMySQL(sql)

    def getUserSubInfo(self, param):
        sql = " SELECT s.name,s.id FROM user_sub as us \
                INNER JOIN subscribe as s \
                ON us.subscribe_id = s.id \
                WHERE us.uid = %s and us.status=1 "
        return self.db.exeAllMySQL(sql, param)

    def getSubInfo(self, param):
        sql = " SELECT * FROM subscribe WHERE name = %s or id = %s "
        return self.db.exeOneMySQL(sql, param)

    def InsertUserSubInfo(self, param):
        sql = " INSERT INTO user_sub (uid,subscribe_id,status) values(%s,%s,%s) "
        self.db.insertMySQL(sql, param)

    def updateUserSubInfo(self, param):
        sql = " UPDATE user_sub SET status = %s WHERE uid = %s and subscribe_id = %s "
        self.db.updateMySQL(sql, param)

    def isSubUserInfo(self, param):
        sql = " SELECT * FROM user_sub WHERE uid = %s and subscribe_id = %s "
        return self.db.exeOneMySQL(sql, param)

    def getSubList(self):
        sql = " SELECT * FROM subscribe WHERE status=1 "
        return self.db.exeAllMySQL(sql)
