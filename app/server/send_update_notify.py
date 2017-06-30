#coding:utf-8
from wechat_sender.sender import Sender
from app.server import userDb


class VerUpdateSend(object):
    def __init__(self,nick_name):    
        self.sender = Sender()
        self.userdbSer = userDb.User()
        self.nick_name = nick_name        
        
    def sendMsg(self,info):
        totalFrineds = self.userdbSer.getToalUserInfo()
        for friend in totalFrineds:
            if self.nick_name != True and friend['nick_name'] == self.nick_name:
                self.sender.send_to(info, search={'nick_name':friend['nick_name'],'user_name':friend['user_name']})
                break
            elif self.nick_name == True:
                self.sender.send_to(info, search={'nick_name':friend['nick_name'],'user_name':friend['user_name']})

        
        