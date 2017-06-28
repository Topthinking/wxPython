from app.server.send_update_notify import VerUpdateSend

if __name__ == '__main__':
    wx_send = VerUpdateSend("sunny严")
    wx_send.sendMsg("老婆，我爱你！么么哒！")
