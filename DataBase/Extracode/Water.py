from plyer import notification 
from time import sleep

while True:
  
    notification_title = 'Amanat Drink Water!!!'  
    notification_message = 'or you have constipution.!!!\n\n          . \n\n         \n            \n'

    notification.notify(  
        title = notification_title,
        message = notification_message,  
        app_icon = None,  
        timeout = 10,
        )
    hour = 60*60
    sleep(hour)