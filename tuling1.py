# -*- coding:utf-8 -*-
# import json
# import socket
# import uuid
# from urllib.request import urlopen,Request
# from urllib.parse import urlencode
#
# class TuringChatMode(object):
#     def __init__(self):
#         self.turing_url = 'http://www.tuling123.com/openapi/api?'
#         self.app_key = '82622364a28142878dd8ad634eec401c'
#
#     def getTuringText(self,text):
#         user_ip = self.getHostIp()
#         mac_id = self.getMacId()
#         turing_url_data = dict(
#             key=self.app_key,
#             info=text,
#             userid=mac_id
#         )
#         request = Request(self.turing_url + urlencode(turing_url_data))
#         try:
#             w_data = urlopen(request)
#         except Exception as error_info:
#             return error_info
#         response_text = w_data.read().decode('utf-8')
#         json_result = json.loads(response_text)
#         return json_result['text']
#
#     def getHostIp(self):
#         socket_info = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#         socket_info.connect(('8.8.8.8',80))
#         ip = socket_info.getsockname()[0]
#         return ip
#
#     def getMacId(self):
#         node = uuid.getnode()
#         mac = uuid.UUID(int=node).hex[-12:]
#         return mac
#
# if __name__ == '__main__':
#     print('您可以和机器人聊天了（退出请输入q）')
#     turing = TuringChatMode()
#     while True:
#         msg = input('\n我：')
#         if msg == 'q':
#             exit('聊天结束！')
#         else:
#             turing_data = turing.getTuringText(msg)
#             print('机器人：',turing_data)
#
#



import requests
import uuid
import json

class turingBot(object):
    def __init__(self):
        self.url = 'http://openapi.tuling123.com/openapi/api/v2'
        self.apikey = '9996ce9ff56c458dadfd74aa0bab6532'

    def getMacId(self):
        node = uuid.getnode()
        mac = uuid.UUID(int=node).hex[-12:]
        return mac

    def getBotText(self,text):
        data = {
            "reqType":0,
            "perception": {
                "inputText": {
                    "text": text
                },
                "inputImage": {
                    "url": "imageUrl"
                },
                "selfInfo": {
                    "location": {
                        "city": "北京",
                        "province": "北京",
                        "street": "信息路"
                    }
                }
            },
            "userInfo": {
                "apiKey": self.apikey,
                "userId": self.getMacId(),
            }
        }
        response = requests.post(self.url,data=json.dumps(data))
        result = response.json()
        # return result
        return result['results'][0]['values']['text']


if __name__ == '__main__':
    print('您可以和图灵机器人聊天了（退出请按q）')
    turing = turingBot()
    while True:
        msg = input('\n我：')
        if msg == 'q':
            exit('聊天结束！')
        else:
            turing_text = turing.getBotText(msg)
            print('机器人：',turing_text)

























































































