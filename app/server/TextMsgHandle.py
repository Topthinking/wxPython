#coding:utf-8
#消息处理，文本消息
from app.common import function
from app.server import userDb,subscribe

import sys

class TextMsg(object):
    def __init__(self):
        self.common = function.CommonFn()
        self.userdbSer = userDb.User()
        pass
    
    def start(self,msg):
        #判断用户的订阅的哪些信息
        #self.common.prn_obj(msg)
        
        msg.chat.send('已接收数据，正在处理中...')
        
        param = (msg.raw["FromUserName"],)
        data = self.userdbSer.getUserInfoByUserName(param)
        
        userId = data["id"]
        
        if msg.text == "我的订阅":
            
            self._mySubList(userId,msg)
        
        else:
            #判定是否是请求订阅，格式：订阅:[斗鱼直播]
            sub = msg.text.split(":")
            
            if sub[0] == "订阅":
                #订阅功能
                self._addSub(sub, userId, msg)     
            elif sub[0] == "取消订阅":
                #取消订阅功能         
                self._cancelSub(sub, userId, msg)     
            else:
                #信息请求        
                #获取订阅信息
                param = (data["id"],)
                subData = self.userdbSer.getUserSubInfo(param)
                
                if len(subData) == 0:
                    info = self._replay_subInfo()
                    msg.chat.send("您需要订阅\n"+info)
                else: 
                    #前往订阅类，处理订阅对应的信息请求
                    subscribe.SubscribeHandle(subData,msg)
                                  
                        
    def _addSub(self,sub,userId,msg):
        subName = sub[1]
        param = (subName,subName)
        subInfo = self.userdbSer.getSubInfo(param)
        if subInfo is None:
            info = self._replay_subInfo()
            msg.chat.send("订阅名称：【"+subName+"】系统还未提供\n"+info);
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
                #更新添加
                if str(isSub["status"]) == "1":
                    msg.chat.send("您已经订阅：【"+subInfo["name"]+"】")
                else:
                   param = (1,userId,subInfo["id"])
                   self.userdbSer.updateUserSubInfo(param) 
                   msg.chat.send("订阅：【"+subInfo["name"]+"】成功，可以使用其功能")
    
    def _cancelSub(self,sub, userId, msg):
        subName = sub[1]
        param = (subName,subName)
        subInfo = self.userdbSer.getSubInfo(param)
        if subInfo is None:
            info = self._replay_subInfo()
            msg.chat.send("订阅名称：【"+subName+"】系统还未提供\n"+info);
        else:
            #判定有没有订阅该项目
            param = (userId,subInfo["id"])
            isSub = self.userdbSer.isSubUserInfo(param)
            
            if isSub is None:
                info = self._replay_subInfo()
                msg.chat.send("您还未订阅：【"+subInfo["name"]+"】\n"+info)
            else:
                #取消订阅
                #uid,subsribe_id,status
                param = (0,userId,subInfo["id"])
                self.userdbSer.updateUserSubInfo(param)
                msg.chat.send("取消订阅：【"+subInfo["name"]+"】成功")                   
                
    def _mySubList(self,userId,msg):
        param = (userId,)
        subData = self.userdbSer.getUserSubInfo(param)
        
        if len(subData) == 0:
            info = self._replay_subInfo()
            msg.chat.send("您还未进行订阅\n"+info)
        else: 
            #列出我的订阅
            info = '[咖啡]我的订阅列表：\n'
            count = 1
            for sub in subData:
                info = info+str(count)+"、订阅号："+str(sub["id"])+"；订阅名："+str(sub["name"])+"\n"
                count = count + 1
            
            sysInfo = self._replay_subInfo()
            
            msg.chat.send(info+sysInfo)
        pass
    
    def _replay_subInfo(self):
        #获取目前可以订阅的功能
        subs = self.userdbSer.getSubList()
        
        info = '[拳头]当前系统可用订阅类型：\n'
        count = 1
        for sub in subs:
            info = info+str(count)+"、订阅号："+str(sub["id"])+"；订阅名："+str(sub["name"])+"\n"
            count = count + 1
            
        info = info + "\n您可以回复: 订阅:[订阅号,订阅名] 例如: 订阅:"+str(subs[0]["name"])
        info = info + "\n把订阅改为取消订阅，其余不变，即可完成取消 "
        info = info + "\n回复：我的订阅  即可查询当前订阅内容\n[爱心]谢谢使用[爱心]"
        return info
        
        
        
        
        
        
                