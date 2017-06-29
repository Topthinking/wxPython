from app.server.main import ServerController

if __name__ == '__main__':
    wx_server = ServerController(False)
    wx_server.replay()
    wx_server.start()