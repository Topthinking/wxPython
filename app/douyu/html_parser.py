# coding:utf-8
from bs4 import BeautifulSoup
import json


class HtmlParser(object):
    def __init__(self):
        self.liveRoom = []
        self.attentionRoom = []

    def _get_live_room(self, soup):

        lists = soup.find_all("li")

        if lists is None or len(lists) == 0:
            return

        cur_rooms = []

        for _list in lists:
            rInfo = _list.find("a")
            if "data-rid" not in rInfo.attrs:
                continue
            rid = rInfo.attrs["data-rid"]
            rName = rInfo.attrs["title"]

            uNameInfo = rInfo.find("span", class_="dy-name")
            if uNameInfo is None:
                rUace = '-未识别-'
            else:
                rUace = uNameInfo.get_text()

            rNumber = rInfo.find("span", class_="dy-num")
            if rNumber is None:
                rNum = 0
            else:
                rNum = rNumber.get_text()

            tmpRoom = {
                "roomId": rid,
                "roomName": rName,
                "nickName": rUace,
                "roomNum": rNum
            }

            self.liveRoom.append(tmpRoom)

            cur_rooms.append(tmpRoom)

        return cur_rooms

    def getLiveRoom(self):
        return self.liveRoom

    def clearAttentionRoom(self):
        self.attentionRoom = []

    def getAttentionRoom(self):
        return self.attentionRoom

    def parse(self, html_cont):

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8")

        return self._get_live_room(soup)

    def jsonParse(self, content):

        roomsData = json.loads(content["$ROOM.showData"])

        print(roomsData["child_cate"]["url"])

        return

        # 已开播
        if roomInfo["show_status"] == 1:
            self.attentionRoom.append({
                "roomId": str(roomInfo['room_id']),
                "roomName": roomInfo['room_name'],
                "nickName": roomInfo['owner_name'],
                "roomNum": roomInfo['levelInfo']['upgrade_exp']
            })

    @staticmethod
    def liveDataByRoomIdParse(content):

        roomInfo = json.loads(content["$ROOM"])

        roomshowData = json.loads(content["$ROOM.showData"])

        if "child_cate" not in roomshowData:
            search_url = roomshowData["game"]["url"]
        else:
            search_url = roomshowData["child_cate"]["url"]

        return {
            "roomId": str(roomInfo['room_id']),
            "roomName": roomInfo['room_name'],
            "nickName": roomInfo['owner_name'],
            "show_status": roomInfo["show_status"],
            "search_url": search_url
        }
