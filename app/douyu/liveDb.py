#coding:utf-8
from app.db import DBmain


class LiveDb(object):
    
    def __init__(self):
        self.db = DBmain.DBModel()
    
    def searchLiveState(self,param):
        sql = " SELECT * FROM dyLiveRoom WHERE alias LIKE %s "
        return self.db.exeAllMySQL(sql,param)
    
    def addLiveState(self,param):
        sql = "INSERT INTO dyLiveRoom (name,roomID,alias) values(%s,%s,%s)"
        return self.db.insertMySQL(sql,param)
    
    def isExistLive(self,param):
        sql = " SELECT * FROM dyLiveRoom WHERE roomId = %s ";
        return self.db.exeOneMySQL(sql,param)
    
    def updateLiveInfo(self,param):
        sql = " UPDATE dyLiveRoom set name=%s,alias=%s WHERE roomId = %s ";
        return self.db.updateMySQL(sql,param)

