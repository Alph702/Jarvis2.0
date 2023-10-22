from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
import pyperclip
from time import sleep
import pyttsx3 as p3

engine = p3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',180)
def Speak(audio):
    print("  ")
    print(f"AI : {audio}")
    print("  ")
    engine.say(audio)
    engine.runAndWait()

sleep(2)
click(x=467, y=54)
hotkey('ctrl','c')
velue = pyperclip.paste()
link = str(velue)

def Download(Link):
    url = YouTube(Link)
    video = url.streams
    video[2].download('F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\Youtube\\')


Speak("Your video is Downloading Sir..")
Download(link)
Speak("Done Sir, I Have Download The Video.")