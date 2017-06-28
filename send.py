from app.server.send_update_notify import VerUpdateSend

if __name__ == '__main__':
    wx_send = VerUpdateSend(True)
    wx_send.sendMsg("欢迎使用top机器人，更多信息访问https://github.com/Topthinking/wxPython/")