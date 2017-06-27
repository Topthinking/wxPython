from server.main import ServerController
import pymysql

if __name__ == '__main__':
    conf = {
        "host":"127.0.0.1",
        "port":3306,
        "user":"root",
        "passwd":"root",
        "db":"test",
        "charset":"utf8",
        "cursorclass":pymysql.cursors.DictCursor
    }
    wx_server = ServerController(True)
    wx_server.setDBconf(conf)
    wx_server.replay()
    #wx_server.start()
    wx_server.Bjoin()