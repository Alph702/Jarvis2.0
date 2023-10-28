import os
import eel

os.startfile("Main.py")

eel.init("www")
os.system('start chrome.exe --app="http://localhost:8000/index.html"')
eel.start("index.html", mode=None, host='localhost', block=True)
