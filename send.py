from app.server.send_update_notify import VerUpdateSend

if __name__ == '__main__':
    wx_send = VerUpdateSend("Always online")
    wx_send.sendMsg("您好")