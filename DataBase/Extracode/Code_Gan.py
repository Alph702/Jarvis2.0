from Code_Gan_Api import MainExecution
import pyttsx3 as p3

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

query = open("F:\\Code\\Jarvis all in one\\Jarvis all in one\\Data.txt",'r')
Writh =  query.read()
query.close()

MainExecution(Writh)

Speak("Sir Your code is saved on Jarvis all in one\DataBase\Gan_Code\Code.txt")