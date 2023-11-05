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

def Python_Setup(foldername):
    def createFolder(foldername):
        pag.click(x=217, y=791)
        sleep(7)
        pag.doubleClick(x=839, y=366,interval=0.2)
        sleep(1)
        pag.doubleClick(x=219, y=257,interval=0.2)
        sleep(1)
        pag.doubleClick(x=1024, y=242,interval=0.2)
        sleep(1)
        pag.click(x=487, y=105)
        sleep(1)
        pag.write(foldername,0.5)
        sleep(0.5)
        pag.keyDown('return')
        pag.keyUp('return')
        sleep(0.5)
        pag.keyDown('return')
        pag.keyUp('return')
        sleep(1)
        pag.click(x=505, y=157)
        sleep(0.5)
        pag.write("cmd",interval=0.2)
        sleep(0.5)
        pag.keyDown('return')
        pag.keyUp('return')
        sleep(0.5)
        pag.write("code .")
        sleep(0.5)
        pag.keyDown('return')
        pag.keyUp('return')

    def openmiro():
        web.open("https://miro.com/app")
        sleep(60)
        pag.click(x=506, y=323)
        sleep(4)
        pag.click(x=552, y=589)

    createFolder(foldername=foldername)
    # sleep(60)
    # openmiro()



Speak("Enter a project folder name")
us = input("Enter a project folder name: ")
Python_Setup(str(us))