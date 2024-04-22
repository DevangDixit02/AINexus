import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import webbrowser
import datetime
import pyttsx3
import os.path
import requests
import wolframalpha

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
engine.setProperty('rate', 150) 
engine.setProperty('volume', 1.0)

inidir=os.path.realpath('history')



def speak(text):
    engine.say(text)
    engine.runAndWait()


def recordaudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening.")
        speak("I am listening.")
        audio = r.listen(source)
    data = ""
    try:

        data = r.recognize_google(audio)
        print("You said: " , data)
        obj = open(completeName,'a+')
        obj.write(data)
    except sr.UnknownValueError:
        print("Sorry. Could not recognise the audio.")
        time.sleep(7)
    except sr.RequestError as e:
        print("You are not connected to the internet.".format(e))
        speak("You are not connected to the internet.".format(e))
        os.system("pause")
    return data


def Nexus(data):
    if "tell me the time" in data:
        strtime=datetime.datetime.now().strftime("%H:%M:%S\n")
        speak(f"the time is {strtime}")
        obj = open(completeName,'a+')
        obj.write('\n')
        obj.write(strtime)
        print(strtime)
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on "+nam+", I will show you where " + location + " is.")
        webbrowser.open_new_tab('https://www.google.co.in/maps/place/'+ location)
        obj = open(completeName,'a+')
        obj.write(location)
        print('I found',location)
    if "open" in data:
        data = data.split(" ")
        op = data[1]
        speak("openng"+op)
        webbrowser.open_new_tab('https://www.'+ op +'.com')
        obj = open(completeName,'a+')
        obj.write(op)
    if "exit" in data:
        print("Thank you for having me.")
        speak("Thank you for having me.")
        time.sleep(2)
        exit()
    if "show today's news" in data:
        webbrowser.open_new_tab('https://news.google.com/topstories')
        obj = open(completeName,'a+')
        obj.write('news\n')
    if "search" in data:
        data=data.split(" ")
        ss=data[1:]
        webbrowser.open_new_tab('https://www.google.co.in/search?q='+str(ss))
        obj = open(completeName,'a+')
        obj.write(str(data))
    if 'find' in data:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=recordaudio()
            app_id="4Y54E6-PARTUHG742"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            obj = open(completeName,'a+')
            obj.write(question)
            obj.write(answer)
time.sleep(3)
nam = input("Enter your name:")

completeName = os.path.join(inidir, nam+".txt") 
obj = open(completeName,'a+')
obj.write('user name:'+ nam)
obj.write('\n')
obj.write('Start time:'+datetime.datetime.now().strftime("%H:%M:%S\n"))
obj.write('\n')
obj.write('End time:'+datetime.datetime.now().strftime("%H:%M:%S\n"))
obj.write('\n')
obj.close()
speak("Hi "+nam+", what can I do for you?")
while 1:
    data = recordaudio()
    Nexus(data)

