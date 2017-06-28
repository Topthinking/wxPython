#coding:utf-8
from app.db import DBmain


class LiveDb(object):
    
    def __init__(self):
        self.db = DBmain.DBModel()
    
    def searchLiveState(self,text):
        sql = " SELECT * FROM dyLiveRoom WHERE alias LIKE '%"+text+"%' "
        return self.db.exeAllMySQL(sql)
    
    def addLiveState(self,param):
        sql = "INSERT INTO dyLiveRoom (name,roomID,alias) values(%s,%s,%s)"
        return self.db.insertMySQL(sql,param)
    
    def isExistLive(self,roomId):
        sql = " SELECT * FROM dyLiveRoom WHERE roomId = "+roomId+" ";
        return self.db.exeOneMySQL(sql)
    
    def updateLiveInfo(self,param,roomId):
        sql = " UPDATE dyLiveRoom set name=%s,alias=%s WHERE roomId ="+roomId+" ";
        return self.db.updateMySQL(sql,param)

