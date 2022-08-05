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
    #Sec2 
    token = 'AluZ73jnEqlv9qUf43hXbDLIN21DYUMurYRIrt1kusJ'
    #Testbot
    #token = 'Eowx3XT2qK5FJf0PQ5BRdFJM80b5hIDx6l55OZ4uEOn'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)

now = datetime.now(timezone('Asia/Bangkok'))
current_time = now.strftime("%H:%M:%S")

print("Current Time =", current_time)
print("Your Time Zone is GMT", strftime("%z", gmtime()))

strMon_1 = "\n9:00 - 12:00 \n\nITLG301 (On-site)\nBusiness Writing\n\n2A : Aj.Paul (Room: IT305)\n2B : Aj.Karl (Room: IT312)\n2C : Aj.Peter C. (Room: IT322)"
strMon_2 = "\n13:00 - 16:00 \n\nITCS451 (On-site)\nArtificial Intelligence\n\nAj.Peter / Aj.Thanapon / Aj.Apirak\n\nRoom: IT322"
strTue_1 = "\n9:00 - 12:00 \n\nITCS361 (On-site)\nManagement Information System\n\nAj.Songsri\n\nRoom: IT322"
strTue_2 = "\n13:00 - 16:00 \n\nITCS420 (On-site)\nComputer Networks\n\nAj.Vasaka / Aj.Assadarat / Aj.Dolvara\n\nRoom: IT322"
strWed_1 = "\n9:00 - 12:00 \n\nITCS414 (On-site)\nInformation Storage and Retrieval\n\nAj.Suppawong\n\nRoom: IT322"
strThu_1 = "\n9:00 - 12:00 \n\nITCS443 (On-site)\nParallel and Distributed Systems\n\nAj.Ekasit\n\nRoom: IT322"
strFri_1 = "\n9:00 - 12:00 \n\nITCS371 (On-site)\nIntroduction to Software Engineering\n\nAj.Thanwadee / Aj.Chaiyong / Aj.Morakot / Aj.Wudhichart\n\nRoom: IT305"

keep_alive()
lineNotify("...Start Line Notify")

while 1 :
    now = datetime.now(timezone('Asia/Bangkok'))
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)

    #monday
    if date.today().weekday() == 0 : 
        if (current_time == "08:45:00") :
            lineNotify(strMon_1)
        if (current_time == "12:45:00") :
            lineNotify(strMon_2)
    #tuesday
    if date.today().weekday() == 1 : 
        if (current_time == "08:45:00") :
            lineNotify(strTue_1)
        if (current_time == "12:45:00") :
            lineNotify(strTue_2)
    #wednesday
    if date.today().weekday() == 2 : 
        if (current_time == "08:45:00") :
            lineNotify(strWed_1)
    #thursday
    if date.today().weekday() == 3 : 
        if (current_time == "08:45:00") :
            lineNotify(strThu_1)
    #friday
    if date.today().weekday() == 4 : 
        if (current_time == "08:45:00") :
            lineNotify(strFri_1)