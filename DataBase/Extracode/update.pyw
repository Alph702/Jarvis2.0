from time import sleep
from os import startfile
import pyttsx3 as p3

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

Speak("Jarvis is updating sir it's may take 1 minute")
sleep(60)
Speak("Jarvis is uptodate")
startfile("F:\\Code\\Jarvis all in one\\Jarvis2.0\\Jarvis.py")
Speak("Jarvis is uptodate")