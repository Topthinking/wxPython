#coding:utf-8
#消息处理，文本消息
from app.common import function
from app.server import userDb,douyuServer

class TextMsg(object):
    def __init__(self):
        self.common = function.CommonFn()
        self.userdbSer = userDb.User()
        pass
    
    def start(self,msg):
        #判断用户的订阅的哪些信息
        #self.common.prn_obj(msg)
        
        param = (msg.raw["FromUserName"],)
        data = self.userdbSer.getUserInfoByUserName(param)
        
        #获取订阅信息
        
        print(data)
        
        #连接斗鱼数据查询
        douyuSer =  douyuServer.DouyuServer(msg)
        
        #根据roomID号爬取斗鱼直播情况
        return douyuSer.liveDataByRoomId()
    