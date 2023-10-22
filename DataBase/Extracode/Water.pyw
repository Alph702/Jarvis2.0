from plyer import notification 
from time import sleep

while True:
  
    notification_title = 'Amanat Drink Water!!!'  
    notification_message = 'or you have constipution.!!!\n\n          . \n\n         \n            \n'  
    icon = r"F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\Gui\\water_115174.ico"  

    notification.notify(  
        title = notification_title,
        message = notification_message,  
        app_icon = icon,  
        timeout = 10,  
        toast = False  
        )
    hour = 60*60
    sleep(hour)