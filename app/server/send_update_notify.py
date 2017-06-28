#coding:utf-8
from wechat_sender.sender import Sender
from app.server import friends

class VerUpdateSend(object):
    def __init__(self,nick_name):
        self.friend_manager = friends.FriendManager()       
        self.sender = Sender()
        self.nick_name = nick_name
        self.friends = self.friend_manager.getFriends(nick_name)
        
        
    def sendMsg(self,info):
        
        for friend in self.friends:
            self.sender.send_to(info, search={'nick_name':friend['nick_name'],'user_name':friend['user_name']})

    