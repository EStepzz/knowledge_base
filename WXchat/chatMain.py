#coding = utf-8
import itchat, time
from itchat.content import *
import requests
import json





def getData(msg):

    apikey='28d8092cb85b4ef2bac1d164c19cbc44'
    api = 'http://openapi.tuling123.com/openapi/api/v2'

    info={
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": ""
            },
            "selfInfo": {
                "location": {
                    "city": "",
                    "province": "",
                    "street": ""
                }
            }
        },
        "userInfo": {
            "apiKey": apikey,
            "userId": "3142536712"
        }
    }
    info = json.dumps(info)
#    print (info)
    rep = requests.post(api, data = info).json()
    #print (rep['results'][0]['values']['text'])
    return rep['results'][0]['values']['text']

# if __name__=='__main__':
#
#     while True:
#         inp = input("input:")
#         res = getData(inp)
#         print (res)


said = []
@itchat.msg_register([TEXT])
def reply_text(msg):

    print (msg)
    res = getData(msg.text)
    username = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    defaultReq = u'Hello:' + username + ',我是微信个人助手，你可以和我说话了^-^'
    if username in said:
        msg.user.send(res)
    else:
        said.append(username)
        msg.user.send(defaultReq)




itchat.auto_login(enableCmdQR=2)
itchat.auto_login(True)
itchat.run()