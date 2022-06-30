from datetime import date, datetime
from keep_alive import keep_alive
from time import *
import time
from pytz import timezone

#message
def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

#sticker
def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

#setting
def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'urI4RcOBlRjV0wYCcHsa742KGrRVcikcuE4mxfHVlld'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

now = datetime.now(timezone('Asia/Bangkok'))
current_time = now.strftime("%H:%M:%S")

print("Current Time =", current_time)
print("Your Time Zone is GMT", strftime("%z", gmtime()))

str1 = "\n13:00 - 16:00 \n\nITCS343 (Online)\nPrinciples of Operating Systems\n\n [https://teams.microsoft.com/l/channel/19%3aa7a036c206254a7c9b1801ea40d348f1%40thread.tacv2/Section%25202?groupId=96da9da8-9ea8-492d-a5b3-554b896da588&tenantId=9bc585f9-a8b8-431c-9013-efa7b2b40cdf]"
lineNotify("Testing Bot. . .")

keep_alive()

while 1 :
    now = datetime.now(timezone('Asia/Bangkok'))
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)

    #monday
    if date.today().weekday() == 0 : 
        if (current_time == "9:00:00") :
            print("stop")
    #tuesday
    if date.today().weekday() == 1 : 
        if (current_time == "9:00:00") :
            print("stop")
    #wednesday
    if date.today().weekday() == 2 : 
        if (current_time == "9:00:00") :
            print("stop")
    #thursday
    if date.today().weekday() == 3 : 
        if (current_time == "19:52:55") :
            lineNotify(str1)
    #friday
    if date.today().weekday() == 4 : 
        if (current_time == "19:48:30") :
            print("stop")

