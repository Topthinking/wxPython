# coding=utf-8
"""
主入口文件
"""
from app.server.main import ServerController

if __name__ == '__main__':
    wx_server = ServerController(True)
    wx_server.replay()
    wx_server.start()
