#coding:utf-8
#处理斗鱼的数据接口
from douyu import liveDataByRoomId,liveDb

class DouyuServer(object):
    
    def __init__(self,conf,msg): 
        #连接数据库
        self.douyuLiveDb = liveDb.LiveDb(conf)
        self.msg = msg
    
    def liveDataByRoomId(self):
        
        liveSer = liveDataByRoomId.LiveDataByRoomId()
        
        result = ''
        
        lists = self.douyuLiveDb.searchLiveState(self.msg.text)
        
        if len(lists) == 0 :
            return "您的查询超过系统爬取的范围，请提交github，让系统进行爬取"
        
            
        for list in lists:

            liveData = liveSer.attention(list["roomId"])
                
            self.msg.chat.send(self._livereplayInfo(liveData))
            
        return "数据发送完毕！"   
        
    
    def _livereplayInfo(self,liveData):
        
        #正在直播
        if liveData['show_status'] == 1:
            info = "房间名称:【"+liveData['roomName']+"】已开播"\
                   "\n房间号："+liveData['roomId']+\
                   "\n主播昵称："+liveData['nickName']+\
                   "\n人气值："+liveData['roomNum']+\
                   "\n访问：https://www.douyu.com/"+liveData['roomId']+"/"
                   
        else:
            info = "房间名称:【"+liveData['roomName']+"】未开播"\
                   "\n房间号："+liveData['roomId']+\
                   "\n主播昵称："+liveData['nickName']+\
                   "\n访问：https://www.douyu.com/"+liveData['roomId']+"/"
                   
        return info 
    