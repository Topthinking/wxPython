#coding:utf-8

from app.server import douyuServer

class SubscribeHandle(object):
    def __init__(self,data,msg):
        self.data = data
        self.msg = msg
        self._diffSub()
        pass
    
    def _diffSub(self):
        res = False
        for sub in self.data:
            if sub["name"] == "斗鱼直播":
                #连接斗鱼数据查询
                douyuSer =  douyuServer.DouyuServer(self.msg)
                
                #根据roomID号爬取斗鱼直播情况
                douyuSer.liveDataByRoomId()                
                res = True

        if res == False:
            self.msg.chat.send("待开发") 