#this is my library
import speech_recognition as sr
import pyttsx3
from ecapture import ecapture as ec
import os
import datetime
import time
import webbrowser
import subprocess
import json
import requests
#for voice
engin=pyttsx3.init('sapi5')
voice=engin.getProperty('voices')
engin.setProperty('voice', 'voices[0].id')
#this is my functions
def speak(text):
    engin.say(text)
    engin.runAndWait()
def welcome():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12 :
        speak("hello,good morning")
        print("hello,good morning")
    elif hour>=12 and hour<18 :
        speak("hello,good afternoon")
        print("hello,good afternoon")
    else:
        speak("hello,good evning")
        print("hello,good evning")
def takCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
        try:
            statment=r.recognize_google(audio,language='en-in')
            print(f"user said:{statment}\n")
        except Exception as e:
            speak("exuse me,please say that again") 
            return "none"
        return statment
        print("loading your AI personal assistant mind-plus")
        speak("loading your AI personal assistant mind-plus")
welcome()

if __name__=='__main__':
    while True:
        speak("Tell me how can I help you?")
        statment=takCommand()
        #if statment=="":
            #continue
        if "good bye" in statment or "ok bye" in statment or "stop" in statment:
            speak("your personal assistant mind-plus is shutting down,Good bye")
            print("your personal assistant mind-plus is shutting down,Good bye")                    
            break
        elif "open Youtube" in statment:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is running")
            time.sleep(5)
        elif "open Google" in statment:
            webbrowser.open_new_tab("https://www.google.com")
            speak("google is running")
            time.sleep(5)
        elif "open Gmail" in statment:
            webbrowser.open_new_tab("https://gmail.com")
            speak("gmail is running")
            time.sleep(5)
        elif "tell me time" in statment:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strtime}")
        elif "take photo" in statment:
            speak("smile please")
            time.sleep(2)
            ec.capture(0,"robo camera",False)
        elif "show me Tehran weather" in statment:
            webbrowser.open_new_tab("https://www.irimo.ir/far/wd/701-%D9%BE%DB%8C%D8%B4-%D8%A8%DB%8C%D9%86%DB%8C-%D9%88%D8%B6%D8%B9-%D9%87%D9%88%D8%A7%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86.html?id=17561")
        elif "tell me about yourself" in statment:
            speak("my name is Mind-plus and I am is a sample of A-I or artificioal Intelligence whit same library and same line code with python language")