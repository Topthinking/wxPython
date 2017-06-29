#coding:utf-8
import pymysql

class Config(object):
    
    def database(self):
        return {
           "host":"116.62.120.178",
        "port":3306,
        "user":"topthinking",
        "passwd":"!woSHIsyj@",
            "db":"spider",
            "charset":"utf8",
            "cursorclass":pymysql.cursors.DictCursor
        }