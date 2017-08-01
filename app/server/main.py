'''
初始化机器人，以及响应好友消息请求
'''
# coding:utf-8
import datetime
import time

from wechat_sender.listener import listen
from wxpy.api.bot import Bot
from app.common import function
from app.server import userDb, TextMsgHandle
'''
微信个人服务器类
'''


class ServerController(object):
    def __init__(self, init=False):
        # 初始化机器人
        self.bot = Bot(init)
        self.bot.enable_puid("wxpy_puid.pkl")
        self.common = function.CommonFn()
        self.userdbser = userDb.User()
        self.textmsg = TextMsgHandle.TextMsg()

        # 存储所有朋友
        self.friends = []

        # 获取朋友列表
        self._get_friend()

    def _get_friend(self):
        friends = self.bot.friends()
        # 遍历所有好友，进行存储和更新好友信息
        friendpuid = set()

        for friend in friends:
            # 判断重复的puid
            if friend.puid in friendpuid:
                continue

            friendpuid.add(friend.puid)
            tmp_friends = self.bot.friends().search(puid=friend.puid)

            for tmp_friend in tmp_friends:

                # 机器人自己不加入
                if tmp_friend.raw["UserName"] == self.bot.self.raw["UserName"]:
                    continue

                # 刷新当前数据库好友信息
                self._actionUserInfo(tmp_friend)

    def start(self):
        print("【" + self.bot.self.raw["NickName"] + "】登录成功")
        listen(self.bot, self.friends)
        self.bot.join()

    def replay(self):
        @self.bot.register()
        def print_others(msg):
            print(msg)

        @self.bot.register(self.friends)
        def reply_my_friend(msg):
            # 添加好友的提示
            if msg.type == "Note":
                return ''

            if msg.type != "Text":
                return "暂时支持文本格式的"

            # 发送的文本信息
            if msg.type == "Text":
                self.textmsg.start(msg)

        @self.bot.register(msg_types="Friends")
        def auto_accept_friends(msg):
            if "top" in msg.text.lower():
                new_friend = msg.card.accept()

                # 对添加的用户进行保存
                self._actionUserInfo(new_friend)

                new_friend.send(
                    '您好，已经接受好友请求了\n访问     https://github.com/Topthinking/wxPython 查看更多'
                )

    def _actionUserInfo(self, friend):
        """
                            添加用户
        nick_name,user_name,puid,add_time
                            更新用户
        nick_name,user_name,puid,update_time,id
        """
        curTime = int(time.mktime(datetime.datetime.now().timetuple()))
        # 判定该添加的朋友之前是否存在备注
        if friend.raw["RemarkName"] == '':
            # 添加新的朋友到数据库
            param = (friend.raw["NickName"], friend.raw["UserName"],
                     friend.puid, curTime)
            remarkName = self.userdbser.insertUserGetInertId(param)
            self.bot.core.set_alias(
                userName=friend.raw["UserName"], alias=remarkName)
        else:
            # 更新
            # 1.先查询是否存在该用户 存在就更新 否则就添加
            param = (friend.raw["RemarkName"], )
            info = self.userdbser.isExistUser(param)

            if info is None:
                # 添加新的朋友到数据库
                param = (friend.raw["NickName"], friend.raw["UserName"],
                         friend.puid, curTime)
                remarkName = self.userdbser.insertUserGetInertId(param)
                self.bot.core.set_alias(
                    userName=friend.raw["UserName"], alias=remarkName)
            else:
                param = (friend.raw["NickName"], friend.raw["UserName"],
                         friend.puid, curTime, friend.raw["RemarkName"])
                self.userdbser.updateUserInfo(param)

        self.friends.append(friend)
