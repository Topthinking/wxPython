#coding:utf-8
from wechat_sender.sender import Sender

from server import friends

from douyu import main
import threading
import time


class WxSend(object):
    def __init__(self,nick_name):
        self.friend_manager = friends.FriendManager()       
        self.sender = Sender()
        self.douyuLive = main.SpilerLiveMain()
        
        self.friends = self.friend_manager.getFriends(nick_name)
        
    def sendMsg(self,info,nick_name):
        
        if len(self.friends) > 1:
            for friend in self.friends:
                self.sender.send_to(info, search={'nick_name':friend['nick_name'],'user_name':friend['user_name']})
                break
        else:
            self.sender.send_to(info, search={'nick_name':nick_name})
        
        print("消息已经成功发送给",nick_name)

    def LiveData(self,nick_name):
        liveData = self.douyuLive.craw(2)
        for live in liveData:
            info = "房间名称:"+live['roomName']+\
                     "\n房间号："+live['roomId']+\
                     "\n主播昵称："+live['nickName']+\
                     "\n人气值："+live['roomNum']+\
                     "\n访问：https://www.douyu.com/"+live['roomId']+"/"
            time.sleep(10)
            print("消息发送中...")
            self.sendMsg(info,nick_name)
            
    def attentionData(self,rooms):
        liveData = self.douyuLive.attention(rooms)
        if len(liveData) ==0 :
            return
        
        for live in liveData:
            info = "房间名称:【"+live['roomName']+"】已开播"\
                     "\n房间号："+live['roomId']+\
                     "\n主播昵称："+live['nickName']+\
                     "\n人气值："+live['roomNum']+\
                     "\n访问：https://www.douyu.com/"+live['roomId']+"/"
            #time.sleep(10)
            print("消息发送中...")
            #self.sendMsg(info,nick_name)
            
    def crawAttention(self,rooms):
        liveData = self.douyuLive.crawAttention(rooms)
        if len(liveData) ==0 :
            return
        
        for live in liveData:
            info = "房间名称:【"+live['roomName']+"】已开播"\
                     "\n房间号："+live['roomId']+\
                     "\n主播昵称："+live['nickName']+\
                     "\n人气值："+live['roomNum']+\
                     "\n访问：https://www.douyu.com/"+live['roomId']+"/"
            #time.sleep(10)
            print("消息发送中...")
            self.sendMsg(info,nick_name)
        
if __name__ == '__main__':
    nick_name= "Always online"
    rooms = ["64609","507882"]
    send_douyu = WxSend(nick_name)
    #send_douyu.LiveData(nick_name)
    #send_douyu.attentionData(rooms)
    send_douyu.crawAttention(rooms)
    
    