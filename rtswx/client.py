import requests
import json

class RtsWXHTTP:
    def __init__(self, url, wxid):
        self.url = url
        self.wxid = wxid
        self.__headers = {'Content-Type': 'application/json'}

    def send_msg(self, user_name: str, content: str, msg_type: int = 1, at_users: str = "", timeout: int = 10):
        data = {
            "ToUserName": user_name,
            "Content": content,
            "MsgType": msg_type,
            "AtUsers": at_users
        }

        params = {
            "funcname": "SendMsg",
            "timeout": timeout,
            "wxid": self.wxid,
        }

        try:
            response = requests.post(url=self.url + "/v1/LuaApiCaller", params=params, data=json.dumps(data),  headers = self.__headers)
        except:
            return None

    
        res = response.json()

        return res