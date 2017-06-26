#coding:utf-8
from wechat_sender.listener import listen
from wxpy.api.bot import Bot
from wxpy.api.messages.message import Message

from common import function
from douyu import main,liveDb
from server import friends

class ServerController(object):
    
    def __init__(self,init=False):
        #初始化机器人
        self.bot = Bot(init)
        self.bot.enable_puid("wxpy_puid.pkl")
        self.friend_manager = friends.FriendManager()
        self.common = function.CommonFn()
        self.douyuLive = main.SpilerLiveMain()
        #存储所有朋友
        self.friends = []
        
        #获取朋友列表
        self._get_friend()
            
    #数据库    
    def setDBconf(self,conf):
        self.conf = conf
             
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
        
    def Bjoin(self):
        print("【"+self.bot.self.raw["NickName"]+"】登录成功")
        self.bot.join()
    
    def replay(self):
        @self.bot.register()
        def print_others(msg):
            print(msg)
            
        @self.bot.register(self.friends)
        def reply_my_friend(msg):
            #连接数据库
            self.douyuLiveDb = liveDb.LiveDb(self.conf)
            #查询数据库
            lists = self.douyuLiveDb.searchLiveState(msg.text)
            
            if len(lists) == 0:
                return "目前仅支持斗鱼主播八师傅和鱼鱼风的查询情况，回复8或者yyf即可"
            
            for list in lists:
                if list["name"] == msg.text:
                    self.douyuLive.clearAttention()
                    liveData = self.douyuLive.attention([list["roomId"]])
                    if len(liveData) ==0 :
                        return "未开播"
                
                    #获取已开播的消息
                    liveData = self.douyuLive.crawAttention([list["roomId"]])
                
                    return self.replayInfo(liveData)   
            
                
        @self.bot.register(msg_types="Friends")
        def auto_accept_friends(msg):
            if msg.text == "top":
                new_friend = msg.card.accept()
                #更新朋友列表
                self._get_friend()                
                new_friend.send('您好，已经接受好友请求了')
            
    def replayInfo(self,liveData):
        info = ''
        for live in liveData:
            info = "房间名称:【"+live['roomName']+"】已开播"\
                    "\n房间号："+live['roomId']+\
                    "\n主播昵称："+live['nickName']+\
                    "\n人气值："+live['roomNum']+\
                    "\n访问：https://www.douyu.com/"+live['roomId']+"/"
    
        return info 
                  
        
            
