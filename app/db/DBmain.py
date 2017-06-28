#coding:utf-8
import pymysql
from app.config import config

class DBModel(object):
    def __init__(self):
        self.conf = config.Config()
        
    def _connect(self):
        self.conn = pymysql.connect(**self.conf.database());
    
    def exeAllMySQL(self,sql,data=None):
        self._connect()
        result = ''
        try:
            with self.conn.cursor() as cursor:
                # 执行sql语句，进行查询
                if data == None:
                    cursor.execute(sql)
                else:
                    cursor.execute(sql,data)
                # 获取查询结果
                result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.conn.commit()
        finally:
            self.conn.close();
            
        return result

    def exeOneMySQL(self,sql,data=None):
        self._connect()
        result = ''
        try:
            with self.conn.cursor() as cursor:
                # 执行sql语句，进行查询
                if data == None:
                    cursor.execute(sql)
                else:
                    cursor.execute(sql,data)
                # 获取查询结果
                result = cursor.fetchone()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.conn.commit()
        finally:
            self.conn.close();
            
        return result
    
    def insertMySQL(self,sql,data):
        self._connect()
        try:
            with self.conn.cursor() as cursor:
                # 执行sql语句，进行查询
                cursor.execute(sql,(data))
                
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.conn.commit()
        finally:
            self.conn.close();
            
    def updateMySQL(self,sql,data):
        self._connect()
        try:
            with self.conn.cursor() as cursor:
                # 执行sql语句，进行查询
                cursor.execute(sql,(data))
                
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.conn.commit()
        finally:
            self.conn.close();
            