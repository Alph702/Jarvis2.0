# importing moduls
import pyttsx3 as p3
import speech_recognition as sr
import os

####### SPEAK #########

def Speak(audio,rate : int = 170, text : bool = True):
    engine = p3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',rate)
    if text == True:
        print("  ")
        print(f"AI : {audio}")
        print("  ")
    engine.say(audio)
    engine.runAndWait()

###### Take Command #######
def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(" ")
        print(": Listening.....")
        print(" ")
        r.pause_threshold = 1
        audio = r.listen(source,0,6)
    
    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f': Your Command : {query}\n')

    except:
        return ""
    
    return query.lower()

def TakeCommand_hi():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(" ")
        print(": Listening.....")
        print(" ")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='hi')

        print(f': Your Command : {query}\n')

    except:
        return ""
    
    return query.lower()

def TaskExe():
    try:
        os.startfile("F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\Extracode\\Water.py") # I open water reminder
    except Exception as e:
        Speak(e)
    from Features import vocab
    vocab()

    while True:
        try:
            query = TakeCommand() # storing the TakeCommand() function on line 21 in varible query

            from Automations import ChromeAuto # for Automation of Chrome
            ChromeAuto(query)
            from Automations import YTAuto # for Automation of Youtube
            YTAuto(query)
            from Automations import winAuto
            winAuto(query)

            
            if 'google search' in query: # for google search. I has mane errors
                from Features import GoogleSearch
                GoogleSearch(query)

            elif 'youtube search' in query: # for youtube search
                Query = query.replace("jarvis","")
                query = Query.replace("youtube search","")
                from Features import YouTubeSaerch
                YouTubeSaerch(query)


            elif 'download' in query: # ToDo: Beter video qolity from youtube (✓)
                from Features import DownloadYouTube
                DownloadYouTube()

            elif 'speed' in query: # Speed Test
                from Features import Speed_Test
                Speed_Test()
            
            elif 'code' in query:
                from Features import Code_Gan # function Code_Gan create a code of any thing in any lang.
                Code_Gan(query)
            
            elif 'remind' in query:
                def remind():
                    Speak("Which time that I will remind you sir")
                    time = input("Which time that I will remind: ")
                    Speak("Which thing that I will Remind You Sir")
                    thing = input("Which thing that I will Remind: ")
                    Time = time.replace(" ","")
                    from Features import Remind
                    Remind(Time,thing)
                remind()

            elif 'remember that' in query:
                from Features import Remember
                Remember(query=query)
            
            elif 'tell' in query:
                from Features import Tall
                Tall()

            elif 'my python setup' in query:
                python_setup_flag = False
                if not python_setup_flag:
                    python_setup_flag = True
                    os.startfile("F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\Extracode\\pythonSetup.py")
            
            elif 'update' in query:
                from Features import update
                update()
            
            elif 'exit' in query:
                quit()

            else: # if i say Nothing to jarvis it print None
                print(None)

        except Exception as e:
            Speak(e)

def Jarvis():
     # for password
    Speak("Whats the Password Sir.") 
    Pass_User = "221"
    while Pass_User != "##amanat##":
        Pass_User = input("Whats the Password: ")
        if Pass_User == "##amanat##": # you can change password by changing this
            TaskExe()
        else:
            Speak("Wrong Password Sir.")


def greet():
    from time import strftime
    time = strftime("%H:%M:%S")
    if time <= "12:00:00":
        Speak("Good Morning Sir..",rate = 190)
    elif time <= "18:00:00":
        Speak("Good Afternoon Sir..",rate = 170)
    elif time <= "20:00:00":
        Speak("Good Evening Sir..",rate = 150)
    else:
        Speak("Good Night Sir..",rate = 80)



if __name__ == '__main__':
    greet()
    TaskExe()