import pywhatkit
import wikipedia
from pywikihow import search_wikihow
import os
import pyttsx3 as p3
import webbrowser as web
from time import sleep
import pyautogui as pag

####### SPEAK #########

def Speak(audio,rate : int = 170):
    engine = p3.init('sapi5')
    voices = engine.getProperty('voices')   
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',rate)
    print("  ")
    print(f"AI : {audio}")
    print("  ")
    engine.say(audio)
    engine.runAndWait()

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("google search","")
    query = query.replace("how to","")
    query = query.replace("What do you mean by","")
    writeab = str(query)

    oooooo = open("F:\\Code\\Jarvis all in one\\Jarvis2.0\\Data.txt",'a')
    oooooo.write(writeab)
    oooooo.close()


    Query = str(term)
    os.startfile('F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\Extracode\\start.py')
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query,max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Speak(how_to_func[0].summary)

    else:
        try:
            search = wikipedia.summary(Query,2)
            Speak(f"According To Your Search : {search}")
        except Exception as e:
            Speak('Error ...Error...Sorry form Jarvis sir')
            return e

def YouTubeSaerch(term):
    result = f"https://www.youtube.com/results?search_query={term}"
    web.open(result)
    Speak("This is What I found For Your Search.")
    try:
        pywhatkit.playonyt(term)
        Speak("This May Also Help you Sir.")
    except Exception as e:
        Speak("Error...Sorry from Jarvis sir.")
        return e

def Alarm(query): # Not integrated to Main file

    TimeHere = open("F:\\Code\\Jarvis all in one\\Jarvis2.0\\Data.txt",'a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\Extracode\\Alarm.py")

def DownloadYouTube():
    os.startfile("F:\\Code\\Jarvis all in one\\Jarvis2.0\\\DataBase\\Extracode\\Yt.py")

def Speed_Test():
    os.startfile("F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\Gui Program\\SpeedTestGui.py")

def Wolfram(query): # It not work in Pakistan
    import wolframalpha
    api_key = "KHYKUV-6XX57V3VTP"
    client = wolframalpha.Client(api_key)
    res = client.query(query)
    
    try:
        Ans = next(res.result).text
        return Ans
    except:
        Speak("An String Velue Is Not Answerable, sir.")

def Colculater(query): # It not work in Pakistan
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divided by","/")
    Final = str(Term)
    
    try:
        result = Wolfram(Final)
        Speak(result)
    except Exception as e:
        Speak('Error...Error...Sorry form Jarvis sir')
        return e

def Code_Gan(query:str):
    a = open("F:\\Code\\Jarvis all in one\\Jarvis2.0\\Data.txt",'w')
    a.write(query)
    a.close()
    os.startfile("F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\Extracode\\Code_Gan.py")

def Remind(Time,Thing):

    while True:
        Time = str(Time)
        Thing = str(Thing)
        from time import strftime
        time = strftime("%I:%M:%S")
        if time == Time:
            from plyer import notification 

            notification_title = 'Remember!!!'  
            notification_message = Thing 

            notification.notify(  
                title = notification_title,
                message = notification_message,  
                app_icon = None,  
                timeout = 10,  
                toast = False  
                )
            Speak( f"Remember Sir {Thing}",rate = 150 )
            break
            

        else:
            pass

def Remember(query):
    Query = query.replace("jarvis","")
    Query = Query.replace("remember","")
    Query = Query.replace("that","")

    a = open("F:\\Code\\Jarvis all in one\\Jarvis2.0\\Re.txt",'w')
    a.write(f"      {Query}")
    a.close()

def Tall():
    b = open("F:\\Code\\Jarvis all in one\\Jarvis2.0\\Re.txt",'r')
    c = b.read()
    b.close()
    Speak(f"this is the thing that you want me to Remember:\n {c}")

def update():
    os.startfile("F:\Code\Jarvis all in one\Jarvis2.0\DataBase\Extracode\update.pyw")
    pag.hotkey('win','5')
    pag.click(x=1266, y=0)
