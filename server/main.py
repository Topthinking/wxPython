#coding:utf-8
from wechat_sender.listener import listen
from wxpy.api.bot import Bot
from common import function
from server import friends
from wxpy.api.messages.message import Message
from douyu import main

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
        
        self.bot.join()
    
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
        #print("【"+self.bot.self.raw["NickName"]+"】登录成功")
        listen(self.bot,self.friends)
    
    def replay(self):
        @self.bot.register(self.friends)
        def reply_my_friend(msg):
            #print(msg.text)
            if msg.text == "yyf":
                self.douyuLive.clearAttention()
                liveData = self.douyuLive.attention(["58428"])
                if len(liveData) ==0 :
                    return "未开播"
                
                #获取已开播的消息
                liveData = self.douyuLive.crawAttention(["58428"])
                
                return self.replayInfo(liveData)
            
            
            if msg.text == "8":
                self.douyuLive.clearAttention()
                liveData = self.douyuLive.attention(["64609"])
                if len(liveData) ==0 :
                    return "未开播"
                
                #获取已开播的消息
                liveData = self.douyuLive.crawAttention(["64609"])
                
                return self.replayInfo(liveData)
                
    
    def replayInfo(self,liveData):
        info = ''
        for live in liveData:
            info = "房间名称:【"+live['roomName']+"】已开播"\
                    "\n房间号："+live['roomId']+\
                    "\n主播昵称："+live['nickName']+\
                    "\n人气值："+live['roomNum']+\
                    "\n访问：https://www.douyu.com/"+live['roomId']+"/"
    
        return info               