#coding:utf-8
from idlelib.iomenu import encoding
import json


class FriendManager(object):
    
    def saveFriends(self,info):
        #把数据写入文件
        fileObj = open('friend.txt','w',encoding="utf-8")
        
        friendStr = json.dumps(info)

        fileObj.write(friendStr)
        
        fileObj.close()
        
    def getFriends(self,nickname):
        #读取文件数据
        fileObj = open('friend.txt')
        
        data = fileObj.readline()
        
        friends = json.loads(data)
            
        fileObj.close()
        
        myFriend = []
        
        for friend in friends:
            if nickname == True:
                myFriend.append({
                    "user_name":friend["user_name"],
                    "nick_name":friend["nick_name"]
                    })
            else:
                if friend['nick_name'] != nickname:
                    continue
                else:
                    myFriend.append({
                        "user_name":friend["user_name"],
                        "nick_name":friend["nick_name"]
                        })
     
        return myFriend
    



