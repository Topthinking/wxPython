#coding:utf-8
from db import DBmain


class LiveDb(object):
    
    def __init__(self,conf):
        self.db = DBmain.DBModel(conf)
    
    def searchLiveState(self,text):
        sql = " SELECT * FROM user WHERE alias LIKE '%"+text+"%' "
        return self.db.exeAllMySQL(sql)

