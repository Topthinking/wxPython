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
        
        userId = data["id"]
        #判定是否是请求订阅，格式：订阅:[斗鱼直播]
        sub = msg.text.split(":")
        
        if sub[0] == "订阅":
            #订阅功能
            subName = sub[1]
            param = (subName,subName)
            subInfo = self.userdbSer.getSubInfo(param)
            if len(subInfo) == 0:
                msg.chat.send("订阅：【"+subName+"】系统还未提供");
            else:
                #判定有没有订阅该项目
                param = (userId,subInfo["id"])
                isSub = self.userdbSer.isSubUserInfo(param)
                
                if isSub is None:
                    #添加订阅
                    #uid,subsribe_id,status
                    param = (userId,subInfo["id"],1)
                    self.userdbSer.InsertUserSubInfo(param)
                    msg.chat.send("订阅：【"+subInfo["name"]+"】成功，可以使用其功能")
                else:
                    msg.chat.send("您已经订阅：【"+subInfo["name"]+"】")
        
        elif sub[0] == "取消订阅":
            #取消订阅功能
            subName = sub[1]
            param = (subName,subName)
            subInfo = self.userdbSer.getSubInfo(param)
            if len(subInfo) == 0:
                msg.chat.send("取消订阅：【"+subName+"】系统还未提供");
            else:
                #判定有没有订阅该项目
                param = (userId,subInfo["id"])
                isSub = self.userdbSer.isSubUserInfo(param)
                
                if isSub is None:
                    msg.chat.send("您还未订阅：【"+subInfo["name"]+"】")
                else:
                    #取消订阅
                    #uid,subsribe_id,status
                    param = (userId,subInfo["id"])
                    self.userdbSer.updateUserSubInfo(param)
                    msg.chat.send("取消订阅：【"+subInfo["name"]+"】成功")
                    
        else:
            #信息请求        
            #获取订阅信息
            param = (data["id"],)
            subData = self.userdbSer.getUserSubInfo(param)
            
            if len(subData) == 0:
                msg.chat.send("需要订阅")
            
            else: 
                
                for sub in subData:
                    if sub["name"] == "斗鱼直播":
                        #连接斗鱼数据查询
                        douyuSer =  douyuServer.DouyuServer(msg)
                        
                        #根据roomID号爬取斗鱼直播情况
                        douyuSer.liveDataByRoomId()
                    
                    else:
                        
                        msg.chat.send("待开发")
                        
                        