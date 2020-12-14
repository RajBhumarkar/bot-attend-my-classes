import time
import datetime
from plyer import notification

def notify_me():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    notification.notify(
        title = "Class joined",
        message = "Class joined at "+str(hour)+":"+str(minute),
        timeout = 5 
    )
