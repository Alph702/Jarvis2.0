from os import startfile
from pyautogui import click
from keyboard import press
import webbrowser as wb
import pyautogui as pag
import pyttsx3 as p3
from time import sleep

####### SPEAK #########
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

# I do not have whatsapp
# def WhatsappMsg(name,message):
    
def ChromeAuto(command:str):

    query = str(command)
    if "open chrome" in query:
        startfile("C:\\Program Files\\Google\Chrome\\Application\\chrome.exe")
    elif 'new tab' in query:
        press('ctrl + t')
    elif 'close tab' in query:
        press('ctrl + w')
    elif 'close chrome' in query:
        press('ctrl + q')
    elif 'close all' in query:
        press('ctrl + shift + q')
    elif 'close all tabs' in query:
        press('ctrl + shift + w')
    elif 'new window' in query:
        press('ctrl + n')
    else:
        pass

def YTAuto(command : str):
    if "open youtube" in command:
        wb.open("https://www.youtube.com/")
    elif "play first video" in command:
        click(x=347, y=332)
    elif "play second video" in command:
        click(x=594, y=385)
    elif "play third video" in command:
        click(x=327, y=687)
    elif "play 4th video" in command:
        click(x=594, y=687)
    elif "play fifth video" in command:
        click(x=861, y=687)
    elif "scroll" in command:
        for x in range(21):
            pag.press("down arrow")
    elif "pause" in command:
        pag.press("space")
        Speak("Video is Paused")
    elif "play" in command:
        pag.press("space")
    elif "volume up" in command:
        pag.press("volumeup")

def winAuto(command:str):

    if 'open vs code' in command:
        pag.keyDown('win')
        pag.keyUp('win')
        sleep(0.25)
        pag.write('visual Studio Code',interval=0.1)
        sleep(1.6)
        pag.press('return')
        Speak("Opening Vs Code")