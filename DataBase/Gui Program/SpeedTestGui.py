from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
import sys
import pyttsx3
from SpeedTestUi import Ui_SpeedTest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def run_uit():
    Speak("I Am Checking Speed Sir , Wait For A While .")
    try:
        import speedtest

        speed = speedtest.Speedtest()

        upload = speed.upload()

        correct_Up = int(int(upload)/8000000)

        download = speed.download()

        correct_down = int(int(download)/8000000)

        Speak(f"Downloading Speed Is {correct_down} M B Per Second .")
        Speak(f"Uploading Speed Is {correct_Up} M B Per Second .")
    except:
        Speak("You net is not able for speed test")
    exit()

class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()

    def run(self):
        run_uit()

StartExe = MainThread()

class StartExecution(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_SpeedTest()

        self.ui.setupUi(self)

        self.ui.label = QMovie("F:\\Code\\Jarvis all in one\\Jarvis2.0\\DataBase\\Gui\\speedTest.gif")

        self.ui.gif.setMovie(self.ui.label)

        self.ui.label.start()

        StartExe.start()

App = QApplication(sys.argv)
speedtest = StartExecution()
speedtest.show()
exit(App.exec_())
