#coding:utf-8
from wechat_sender.listener import listen
from wechat_sender.sender import Sender
from wxpy.api.bot import Bot

from app.common import function
from app.server import friends,douyuServer

class ServerController(object):
    
    def __init__(self,init=False):
        #初始化机器人
        self.bot = Bot(init)
        self.bot.enable_puid("wxpy_puid.pkl")
        self.friend_manager = friends.FriendManager()
        self.common = function.CommonFn()

        #存储所有朋友
        self.friends = []
        
        #获取朋友列表
        self._get_friend()
   
    def _get_friend(self):
        friends = self.bot.friends()

        friendpUid = set()
        friendInfo = []
        
        for friend in friends:
            #判断重复的puid
            if friend.puid in friendpUid:
                continue
            
            friendpUid.add(friend.puid)
            
            tmpFriends = self.bot.friends().search(puid=friend.puid)
            
            for tmpFriend in tmpFriends:
                
                #打印所有对象集合
                #self.common.prn_obj(tmpFriend)
                
                friendInfo.append({
                    "user_name":tmpFriend.raw["UserName"],
                    "nick_name":tmpFriend.raw["NickName"],
                    "puid":tmpFriend.puid,
                    "remark_name":tmpFriend.raw["RemarkName"]
                })
                self.friends.append(tmpFriend)
        
        self.friend_manager.saveFriends(friendInfo)
    
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
            if msg.type == "Friends":
                return "访问     https://github.com/Topthinking/wxPython 查看更多"
            
            #连接斗鱼数据查询
            douyuSer =  douyuServer.DouyuServer(msg)
            
            #根据roomID号爬取斗鱼直播情况
            return douyuSer.liveDataByRoomId()
                
        @self.bot.register(msg_types="Friends")
        def auto_accept_friends(msg):
            if msg.text == "top":
                new_friend = msg.card.accept()
                #更新朋友列表
                self._get_friend()                
                new_friend.send('您好，已经接受好友请求了')
            
                  
        
            
