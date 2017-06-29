#coding:utf-8
from wechat_sender.sender import Sender
from app.server import userDb
from wxpy.api.bot import Bot
import time

class VerUpdateSend(object):
    def __init__(self,nick_name):
        self.bot = Bot()     
        self.sender = Sender()
        self.userdbSer = userDb.User()
        
        self.nick_name = nick_name
        self.totalFrineds = self.userdbSer.getToalUserInfo()
        
    def sendMsg(self,info):
        
        print(self.bot.friends())
        
        for friend in self.totalFrineds:
            print(friend)
            #if friend['nick_name'] != 'AAA.top.bot':
            #a = self.sender.send_to(info, search={'nick_name':friend['nick_name'],'user_name':friend['user_name']})
            #print(a)
            

        
        