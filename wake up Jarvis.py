import speech_recognition as sr
import os

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

query = TakeCommand()
if 'wake up Jarvis' in query:
    os.startfile("F:\\Code\\Jarvis all in one\\Jarvis2.0\\Jarvis.py")
else:
    None