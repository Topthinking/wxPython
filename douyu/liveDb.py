#coding:utf-8
from db import DBmain


class LiveDb(object):
    
    def __init__(self,conf):
        self.db = DBmain.DBModel(conf)
    
    def searchLiveState(self,text):
        sql = " SELECT * FROM user WHERE alias LIKE '%"+text+"%' "
        return self.db.exeAllMySQL(sql)
    
    def addLiveState(self,param):
        sql = "INSERT INTO user (name,roomID,alias) values(%s,%s,%s)"
        return self.db.insertMySQL(sql,param)
    
    def isExistLive(self,roomId):
        sql = " SELECT * FROM user WHERE roomId = "+roomId+" ";
        return self.db.exeOneMySQL(sql)

