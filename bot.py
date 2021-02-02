from rtswx.client import RtsWXHTTP

bot = RtsWXHTTP(url="http://127.0.0.1:8898", wxid="wxid_xxxxxxxx")

group_id = "12345678@chatroom"

bot.send_msg(group_id, "你好")
