#coding:utf-8
#根据roomID获取直播详情
import threading

from wechat_sender import Sender

from douyu import url_manager, html_downloader, html_parser
import json
from future.backports.misc import count


class LiveDataByRoomId(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
    
    #根据roomID号获取基本参数
    def attention(self,roomId):
        
        result = ''
        
        try:
            url = "http://www.douyu.com/ztCache/WebM/room/"+str(roomId)
            
            html_cont = self.downloader.download(url)
            
            content = json.loads(html_cont)
            
            if content == []:
                result = None
            
            data = self.parser.liveDataByRoomIdParse(content)
            
            #正在直播，需要获取直播人气值
            if data["show_status"] == 1:
                liveData = self.crawAttention(roomId, data["search_url"])
                data["roomNum"] = liveData["roomNum"]
            else:
                data["roomNum"] = 0
            
            result = data
                    
        except Exception as e:
            print('craw failed:%s' % (e))
        
        return result
    
    #根据分类的url获取具体的人气值  
    
    def crawAttention(self,roomId,child_cate_url):
        
        findNumber = True
        count = 1
        
        result = ''

        while findNumber:
            try:
                url = "https://www.douyu.com"+str(child_cate_url)+"?page="+str(count)+"&isAjax=1"
                
                html_cont = self.downloader.download(url)
                
                roomData =  self.parser.parse(html_cont)
                            
                for roomD in roomData:
                    if roomD["roomId"] == str(roomId):
                        findNumber = False
                        result = roomD
     
                count = count + 1
                
            except Exception as e:
                print('craw failed:%s' % (e))
        
        return result
    
    
    
    
    #根据roomId判定房间是否存在
    
    def isExistRoom(self,roomId):
        url = "http://www.douyu.com/ztCache/WebM/room/"+str(roomId)
            
        html_cont = self.downloader.download(url)
        
        content = json.loads(html_cont)
        
        if content == []:
            result = None
        
        roomInfo = json.loads(content["$ROOM"])
        
        if roomInfo['room_name'] == False:
            return False
        else:
            return True
    