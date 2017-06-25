#coding:utf-8
import threading

from wechat_sender import Sender

from douyu import url_manager, html_downloader, html_parser
import json
from future.backports.misc import count


class SpilerLiveMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        pass

    
    def craw(self,page=10):
        count = 1

        while count<page:
            try:
                url = "https://www.douyu.com/directory/all?page="+str(count)+"&isAjax=1"
                
                html_cont = self.downloader.download(url)
                
                self.parser.parse(html_cont)                
                
                count = count + 1
                
            except Exception as e:
                print('craw failed:%s' % (e))
        
        return self.parser.getLiveRoom()
    
    def attention(self,rooms=[]):
        if len(rooms) == 0:
            return
        
        for room in rooms:
            try:
                url = "http://www.douyu.com/ztCache/WebM/room/"+str(room)
                
                html_cont = self.downloader.download(url)
                
                content = json.loads(html_cont)
                
                if content == []:
                    continue
                
                self.parser.jsonParse(content)                
                    
            except Exception as e:
                print('craw failed:%s' % (e))
        
        return self.parser.getAttentionRoom()
    
    def crawAttention(self,rooms=[]):
        
        if len(rooms) == 0:
            return
        count = 1
        new_rooms = []

        while len(rooms):
            try:
                url = "https://www.douyu.com/directory/all?page="+str(count)+"&isAjax=1"
                
                html_cont = self.downloader.download(url)
                
                roomData =  self.parser.parse(html_cont)                
                
                for roomD in roomData:
                    if roomD["roomId"] in rooms:
                        rooms.remove(roomD["roomId"])
                        new_rooms.append(roomD)
     
                count = count + 1
                
            except Exception as e:
                print('craw failed:%s' % (e))
        
        return new_rooms
    
    def clearAttention(self):
        self.parser.clearAttentionRoom()
    