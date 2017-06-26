#coding:utf-8
import pymysql
class DBModel(object):
    def __init__(self,conf):
        self.conn = pymysql.connect(**conf);
    
    def exeMySQL(self,sql):
        result = ''
        try:
            with self.conn.cursor() as cursor:
                # 执行sql语句，进行查询
                cursor.execute(sql)
                # 获取查询结果
                result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self.conn.commit()
        finally:
            self.conn.close();
            
        return result