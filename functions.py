import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import subprocess
import speech_recognition as sr
import pyautogui
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    minutes = int(datetime.datetime.now().minute)
    if (hour==6 and minutes==0) or (hour==7 and minutes==0) or (hour==8 and minutes==0) or (hour==9 and minutes==0):
        speak("Good Morning! Hope you have a good sleep")

    elif hour==12 and minutes==0:
        speak("Good Afternoon!")   

    elif hour==18 and minutes==0:
        speak("Good Evening!")  

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        query = r.recognize_google(audio)
    except:  
        speak("Say that again please...")  
    return query

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

def find_application_path(application_name):
    for root, dirs, files in os.walk('C:'): 
        if application_name.lower() in [file.lower() for file in files]:
            return os.path.join(root, application_name)
    return None

def open_application(application_name):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite(application_name)
    time.sleep(1)
    pyautogui.press('enter')

if __name__ == '__main__':
    
    wishMe()

    while True:

        query = takeCommand().lower()
        
        if "listen pc what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"the time is {strTime}")

        elif 'listen pc open youtube' in query:
            try:
                webbrowser.get(chrome_path).open("youtube.com")
                speak("opening youtube")
            except:
                webbrowser.open("youtube.com")

        elif 'listen pc open google' in query:
            try:
                webbrowser.get(chrome_path).open("google.com")
                speak("opening google")
            except:
                webbrowser.open("google.com")

        elif 'listen pc open stack overflow' in query:
            try:
                webbrowser.get(chrome_path).open("stackoverflow.com")
                speak("opening stackoverflow")
            except:
                webbrowser.open("stackoverflow.com")  

        elif 'listen pc open mail' in query:
            try:
                webbrowser.get(chrome_path).open("mail.google.com")
            except:
                webbrowser.open("mail.google.com")

        elif "listen pc open riot client" in query:
            try:
                subprocess.Popen("C:\Riot Games\Riot Client\RiotClientServices.exe") 
            except:
                speak("Something went wrong!")

        elif 'listen pc open discord' in query:
            try:
                subprocess.Popen("C:/Users/Lenovo/AppData/Local/Discord/app-1.0.9030/Discord.exe")
            except:
                speak("Something went wrong!")

        elif "listen pc let's code" in query:
            try:
                subprocess.Popen("C:/Users/Lenovo/AppData/Local/Programs/Microsoft VS Code\Code.exe")
            except:
                speak("Something went wrong!")

        elif "listen pc let's play valorant" in query:
            try:
                subprocess.Popen("C:/Riot Games/VALORANT/live/VALORANT.exe")
            except:
                speak("Something went wrong!")

        elif "listen pc open notepad" in query:
            try:
                subprocess.Popen("notepad.exe")
            except:
                speak("something went wrong")
        
        elif "pc shut yourself off" in query:
            speak("pc shutting down, see you soon")
            break


    