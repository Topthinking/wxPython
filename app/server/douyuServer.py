#coding:utf-8
#处理斗鱼的数据接口
from app.douyu import liveDataByRoomId,liveDb

class DouyuServer(object):
    
    def __init__(self,msg): 
        #连接数据库
        self.douyuLiveDb = liveDb.LiveDb()
        self.liveSer = liveDataByRoomId.LiveDataByRoomId()
        self.msg = msg
    
    def liveDataByRoomId(self):
           
        newMsg = self.msg.text.split(":")
        
        #查询
        if len(newMsg) == 0 or newMsg[0] != "dy":  
            
            self.msg.chat.send('已接收数据，正在请求中...')
        
            lists = self.douyuLiveDb.searchLiveState(self.msg.text)
            
            if len(lists) == 0 :
                return "您的查询超过系统爬取的范围\n可以回复格式为\n dy:[名称]:[房间号]:[别名1,别名2,别名3]\n即可完成添加或者修改，目前针对斗鱼直播数据\n例如： dy:yyf:58428:rua,胖头鱼"
            
            searchLive = False
                
            for list in lists:
    
                liveData = self.liveSer.attention(list["roomId"])
                                   
                self.msg.chat.send(self._livereplayInfo(liveData))
                
                searchLive = True
             
            if searchLive == True:   
                return "数据发送完毕！"   
        #插入
        elif len(newMsg) !=0 and newMsg[0] == "dy":
            
            if len(newMsg) != 4:
                return "错误格式的数据"
            
            self.msg.chat.send('已接收数据，正在添加数据...')
            
            #name,roomId,alias
            #dy:top:12345:a,b,v,d
            #newMsg[1],newMsg[2],newMsg[3]
            
            #先判断房间号在斗鱼是否存在
            if self.liveSer.isExistRoom(newMsg[2]) == False:
                return "房间号:【"+newMsg[2]+"】在斗鱼不存在，无法添加"
            
            data = self.douyuLiveDb.isExistLive(newMsg[2])
            
            if data is None:
                
                #添加数据
                param = (newMsg[1],newMsg[2],newMsg[3])

                self.douyuLiveDb.addLiveState(param)
            
                return "数据添加成功"
            
            else:
                
                #更新数据
                alias = data["alias"].split(",")
                
                newAlias = newMsg[3].split(",")
                
                for newAlia in newAlias:
                    if newAlia not in alias:
                        alias.append(newAlia)
                
                alias = ",".join(alias)
                
                #更新房间信息
                param = (newMsg[1],alias)
                
                self.douyuLiveDb.updateLiveInfo(param, newMsg[2])
                
                return "房间号:【"+newMsg[2]+"】数据更新成功！"
        
    
    def _livereplayInfo(self,liveData):
            
        #正在直播
        if liveData['show_status'] == 1:
            info = "房间名称:【"+liveData['roomName']+"】已开播"\
                   "\n房间号："+liveData['roomId']+\
                   "\n主播昵称："+liveData['nickName']+\
                   "\n人气值："+liveData['roomNum']+\
                   "\n访问：https://www.douyu.com/"+liveData['roomId']+"/"
                   
        else:
            info = "房间名称:【"+liveData['roomName']+"】未开播"\
                   "\n房间号："+liveData['roomId']+\
                   "\n主播昵称："+liveData['nickName']+\
                   "\n访问：https://www.douyu.com/"+liveData['roomId']+"/"
                   
        return info 
    