import pywhatkit as py
from datetime import datetime
from keyboard import press

class Sendwhatsappmsg:
    def __init__(self):
        sendwhatmsg()

def sendwhatmsg(pnum,msg):
    now = datetime.now()
    hr = int(now.strftime("%H"))
    min = int(now.strftime("%M")) + 1
    py.sendwhatmsg(pnum,msg,hr,min)
    press('enter')
    return("Msg will be send within 1 min . . . ")