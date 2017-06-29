#coding:utf-8
from wechat_sender.listener import listen
from wechat_sender.sender import Sender
from wxpy.api.bot import Bot
import datetime
import time

from app.common import function
from app.server import userDb,TextMsgHandle


class ServerController(object):
    
    def __init__(self,init=False):
        #初始化机器人
        self.bot = Bot(init)
        self.bot.enable_puid("wxpy_puid.pkl")
        self.common = function.CommonFn()
        self.userdbSer = userDb.User()
        self.textMsg = TextMsgHandle.TextMsg()

        #存储所有朋友
        self.friends = []
        
        #获取朋友列表
        self._get_friend()
   
    def _get_friend(self):
        friends = self.bot.friends()
        
        #遍历所有好友，进行存储和更新好友信息
        friendpUid = set()
        
        for friend in friends:
            #判断重复的puid
            if friend.puid in friendpUid:
                continue
            
            friendpUid.add(friend.puid)
            
            tmpFriends = self.bot.friends().search(puid=friend.puid)
            
            for tmpFriend in tmpFriends:
                
                #打印所有对象集合
                #self.common.prn_obj(tmpFriend)
                
                """
                                        添加用户
                nick_name,user_name,puid,add_time
                                        更新用户
                nick_name,user_name,puid,update_time,id
                """
                curTime = int(time.mktime(datetime.datetime.now().timetuple()))
                remarkName = tmpFriend.raw["RemarkName"]
                
                if tmpFriend.raw["RemarkName"] == '':
                    #添加新的用户                    
                    param = (tmpFriend.raw["NickName"],tmpFriend.raw["UserName"],tmpFriend.puid,curTime)
                    remarkName = self.userdbSer.insertUserGetInertId(param)
                    self.bot.core.set_alias(userName=tmpFriend.raw["UserName"], alias=remarkName)                   
                else:
                    #更新用户
                    param = (tmpFriend.raw["NickName"],tmpFriend.raw["UserName"],tmpFriend.puid,curTime,tmpFriend.raw["RemarkName"])
                    self.userdbSer.updateUserInfo(param)

                self.friends.append(tmpFriend)
        
    def start(self):
        print("【"+self.bot.self.raw["NickName"]+"】登录成功")
        listen(self.bot,self.friends)
        self.bot.join()
        
    def replay(self):
        @self.bot.register()
        def print_others(msg):
            print(msg)
            
        @self.bot.register(self.friends)
        def reply_my_friend(msg):
            #添加好友的提示 
            if msg.type == "Note":
                return ''
                     
            if msg.type != "Text":
                return "暂时支持文本格式的"
            
            #发送的文本信息
            if msg.type == "Text":
                return self.textMsg.start(msg)
            
                
        @self.bot.register(msg_types="Friends")
        def auto_accept_friends(msg):
            if "top" in msg.text.lower():
                new_friend = msg.card.accept()
                
                #添加新的朋友到数据库     
                curTime = int(time.mktime(datetime.datetime.now().timetuple()))
                param = (new_friend.raw["NickName"],new_friend.raw["UserName"],new_friend.puid,curTime)
                remarkName = self.userdbSer.insertUserGetInertId(param)
                self.bot.core.set_alias(userName=new_friend.raw["UserName"], alias=remarkName)
                
                self.friends.append(new_friend)
                  
                new_friend.send('您好，已经接受好友请求了\n访问     https://github.com/Topthinking/wxPython 查看更多')
            
                  
        
            
