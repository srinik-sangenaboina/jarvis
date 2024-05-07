import pyautogui
import pywhatkit as kit
import datetime
import os
import cv2
import random
import ctypes
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
# Python Program to Get IP Address
import socket

import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
#from urllib.request import urlo

import ipaddress
import PyPDF2


import wikipedia as wikipedia
from requests import get
import webbrowser
import simple_webbrowser
import pywhatkit
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisgu import Ui_MainWindow


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)




# --text to speech

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()






#to wish
def wish () :
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if 0 <= hour <= 12:
        speak(f"Good Morning Sri,its {tt}")
    elif 12 < hour < 18:
        speak(f"Good Afternoon Sri,its{tt}")
    else:
        speak(f"Good Evening Sri,its{tt}")


    speak("im jarvis sir. please tell me how can i help you")











def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('sangenaboinar@gmail.com', 'Raju95505@123')
    server.sendmail('sangenaboinar@gmail.com', to, content)
    server.close()

def pdf_reader():
    book = open("C:\\Users\\srinik\\OneDrive\\Documents\\MEFA by Aryasri.pdf " , 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    speak(f'Total number of pages in this book{pages}')
    speak('sir please enter the page number i have to read')
    pg = int(input("please enter the page number"))
    page = pdfReader.pages[pg]
    text =  page.extract_text()
    speak(text)




    ##to convert voice into text

def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=5, phrase_time_limit=8)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")

        except Exception as e:
            speak("say that again please............")
            return "None"
        return query


def start():
        wish()

        #takecommand()
        #speak("This is advanced jarvis")

        while True:
        #if 1:


            query = takecommand().lower()

            #logic building for tasks

            if "open notepad" in query:
                npath= "C:\\Program Files\\Notepad++\\notepad++.exe"
                os.startfile(npath)

            #close an app
            elif "close notepad" in query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad++.exe")

            elif "open instagram" in query:
                ipath = "C:\\Users\\srinik\\OneDrive\\Desktop\\Instagram.lnk"
                os.startfile(ipath)

            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.relaease()
                cv2.destroyAllWindows()
            elif "play music" in query:
                music_dir = ""
                songs = os.listdir(music_dir)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir,song))



            elif "wikipedia" in query:
                speak("searching wikipedia----")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=32)
                speak("according to wikipedia")
                speak(results)
                print(results)

            elif "ip address" in query:

                hostname = get('https://api.ipify.org').text
                IPAddr = socket.gethostbyname(hostname)


                speak(f"Your IP Address is: {IPAddr}")

            elif "youtube" in query:
                webbrowser.open_new('youtube.com')

            elif 'play songs on youtube' in query:

                    speak("Here you go \n")

                    #webbrowser.open("youtube.com")
                    kit.playonyt("see you again")

            elif "open facebook" in query:
                webbrowser.open("www.facebook.com")



            elif "stack overflow" in query:
                webbrowser.open_new('www.stackoverflow.com')

            elif "sleep the system " in query:
                os.system("rund1132.exe powrprof.dll,SetSuspendState 0,1,0")




            elif "send message" in query:
                kit.sendwhatmsg("+919346263852", "poye chusko po rah", 9, 22)





            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                speak(f"Sir, the time is {strTime}")

            elif 'how are you' in query:
                        speak("I am fine, Thank you")
                        speak("How are you, Sir")

            elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")



            #not working

            elif 'email to me' in query:
                try:
                    speak("What should I say?")
                    content = takecommand()
                    to = "sriniksangenaboina@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")



            #not working

            elif 'send a mail' in query:
                try:
                    speak("What should I say?")
                    content = takecommand()
                    speak("whome should i send")
                    to = input()
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()




            elif 'take rest' in query:
                speak("Thank you! im very much tired")
                exit()

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by srinik.")


            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'search' in query or 'play' in query:

                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)
            #not working
            elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif 'open google' in  query:
                speak("opening google!")
                webbrowser.open_new('www.google.com')

            elif "who i am" in  query:
                speak("If you talk then definitely your human.")

            elif "where is" in  query:
                query =  query.replace("where is", "")
                location =  query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")

            elif 'switch windows' in  query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in  query:
                speak("please wait sir,im fetching the latest news")
                #news()

            elif "where i am" in query or "where we are" in query:
                speak("wait sir, let me check once")
                try:
                    ipAdd=requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests=requests.get(url)
                    geo_data=geo_requests.json()
                    #print(geo_data)
                    city=geo_data['city']
                    #state=geo_data['state']
                    country=geo_data['country']
                    speak(f"sir i am not sure,but i think we are in {city} city of {country}")
                except Exception as e:
                    speak("sorry sir, Due to network issue i am not unable to find where we are.")
                    pass


            #take a screenshot

            elif "take screenshot" in query or 'take a screenshot' in query:
                speak('sir ,please tell me the name for this screenshot file')
                name=takecommand().lower()
                speak("please sir hold the screen for few seconds,iam taking screenshot")
                time.sleep(3)
                img=pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i a, done sir, the screenshot is saved in our main folder.now i am ready for next command")


            elif "read pdf" in query:
                pdf_reader()


            elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
                speak('sir please tell me you want to hide this folder or make it visible for everyone')
                condition = takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak('sir,all the files in this folder are now hidden')

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak('sir, all the files in this folder are now visible to everyone')

                elif "leave it" in condition or"leave for me" in condition:
                    speak("ok sir")

if __name__ == "__main__":
    start()




