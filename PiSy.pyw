import tkinter as tk
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import subprocess
import pyautogui
import time
import random
import threading
from PIL import Image, ImageTk
import customtkinter
from pystray import MenuItem as item
import pystray
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)

hour = int(datetime.datetime.now().hour)
minutes = int(datetime.datetime.now().minute)
strTime = datetime.datetime.now().strftime("%H:%M")

def open_application(application_name):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite(application_name)
    time.sleep(1)
    pyautogui.press('enter')

def extract_application_name(command):
    start_index = command.find("application") + len("application") + 1
    end_index = command.find(" ", start_index)
    if end_index == -1:
        end_index = len(command)
    return command[start_index:end_index]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def open_website(website_name):
    url = f"https://www.{website_name}.com"
    webbrowser.open(url)

def extract_website_name(command):
    start_index = command.find("open website") + len("open website") + 1
    return command[start_index:]

def generate_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    return random.choice(jokes)

def press_tab_key(times=1):
    for _ in range(times):
        pyautogui.press('tab')

def listen_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio).lower()
        if "listen pc" in query:
            return True
        
        elif "listen pc what's the time" in query:
            try:
                speak(f"the time is {strTime}")
            except:
                speak("Please repeat.")

        elif "listen pc" and "how are you" in query:
            try:
                speak("Hey there, i am fine. Thank you for asking.")
            except:
                speak("Please repeat.")

        elif "listen pc" and "tell me a joke" in query:
            try:
                speak("Ok, listen carefully.")
                random_joke = generate_random_joke()
                speak(random_joke)
            except:
                speak("Please repeat.")

        elif "listen pc" and 'open youtube' in query:
            try:
                webbrowser.get(chrome_path).open("youtube.com")
                speak("opening youtube")
                press_tab_key(4)
                speak("what you want to search.")
            except:
                speak("Please repeat.")

        elif "listen pc" and 'open google' in query:
            try:
                webbrowser.get(chrome_path).open("google.com")
                speak("opening google")
            except:
                speak("Please repeat.")

        elif "listen pc" and 'open stack overflow' in query:
            try:
                webbrowser.get(chrome_path).open("stackoverflow.com")
                speak("opening stackoverflow")
            except:
                speak("Please repeat.")

        elif "listen pc" and 'open mail'in query:
            try:
                webbrowser.get(chrome_path).open("mail.google.com")
                speak("opening mail")
            except:
                speak("Please repeat.")

        elif "listen pc" and "open application" in query:
            try:
                application_name = extract_application_name(query)
                speak(f"Opening {application_name}...")
                open_application(application_name)
            except:
                speak("Please repeat.")

        elif "listen pc" and "open website" in query:
            try:
                website_name = extract_website_name(query)
                speak(f"Opening {website_name}...")
                open_website(website_name)
            except:
                speak("Please repeat.")

        elif "listen pc" and "thank you" in query:
            try:
                speak("you are most welcome.")
            except:
                pass
        
        elif "listen pc" and "good morning" in query:
            try:
                if hour >= 6 and hour < 12:
                    speak("good morning chief.")
                else:
                    speak(f"hey there, it's {strTime} now")
            except:
                pass

        elif "listen pc" and "good afternoon" in query:
            try:
                if hour >= 12 and hour < 18:
                    speak("good afternoon.")
                else:
                    speak(f"it's {strTime} now")
            except:
                pass

        elif "listen pc" and "good evening" in query:
            try:
                if hour >= 18:
                    speak("good evening.")
                else:
                    speak(f"it's {strTime} now")
            except:
                pass

        elif "listen pc" and "type for me" in query:
            try:
                speak("what you want to type.")
                typeSentence = recognizer.recognize_google(audio).lower()
                pyautogui.typewrite(typeSentence)
            except:
                pass
            
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    return False

def listen_for_commands():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio).lower()
        if "what's the time" in query:
            try:
                speak(f"the time is {strTime}")
            except:
                speak("Please repeat.")

        elif "how are you" in query:
            try:
                speak("Hey there, i am fine. Thank you for asking.")
            except:
                speak("Please repeat.")

        elif "tell me a joke" in query:
            try:
                speak("Ok, listen carefully.")
                random_joke = generate_random_joke()
                speak(random_joke)
            except:
                speak("Please repeat.")

        elif 'open youtube' in query:
            try:
                webbrowser.get(chrome_path).open("youtube.com")
                speak("opening youtube")
                press_tab_key(4)
                speak("what you want to search.")
            except:
                speak("Please repeat.")

        elif 'open google' in query:
            try:
                webbrowser.get(chrome_path).open("google.com")
                speak("opening google")
            except:
                speak("Please repeat.")

        elif 'open stack overflow' in query:
            try:
                webbrowser.get(chrome_path).open("stackoverflow.com")
                speak("opening stackoverflow")
            except:
                speak("Please repeat.")

        elif 'open mail'in query:
            try:
                webbrowser.get(chrome_path).open("mail.google.com")
                speak("opening mail")
            except:
                speak("Please repeat.")

        elif "open application" in query:
            try:
                application_name = extract_application_name(query)
                speak(f"Opening {application_name}...")
                open_application(application_name)
            except:
                speak("Please repeat.")

        elif "open website" in query:
            try:
                website_name = extract_website_name(query)
                speak(f"Opening {website_name}...")
                open_website(website_name)
            except:
                speak("Please repeat.")

        elif "thank you" in query:
            try:
                speak("you are most welcome.")
            except:
                pass
        
        elif "good morning" in query:
            try:
                if hour >= 6 and hour < 12:
                    speak("good morning chief.")
                else:
                    speak(f"hey there, it's {strTime} now")
            except:
                pass

        elif "good afternoon" in query:
            try:
                if hour >= 12 and hour < 18:
                    speak("good afternoon.")
                else:
                    speak(f"it's {strTime} now")
            except:
                pass

        elif "good evening" in query:
            try:
                if hour >= 18:
                    speak("good evening.")
                else:
                    speak(f"it's {strTime} now")
            except:
                pass

        elif "type for me" in query:
            try:
                speak("what you want to type.")
                typeSentence = recognizer.recognize_google(audio).lower()
                pyautogui.typewrite(typeSentence)
            except:
                pass

    except sr.UnknownValueError:
       pass
    except sr.RequestError:
        pass

def commandLine():
    speak('hello.')
    while True:
        if listen_wake_word():
            speak("give me a task.")
            listen_for_commands()

        

    
                
                
root = customtkinter.CTk()
root.title("PiSy")
root.geometry("205x205")
root.resizable(False, False)
root.iconbitmap(default='C:/Users/Lenovo/OneDrive/Desktop/PiSy AI/images/logo.ico')
root.configure(bg="black")
customtkinter.set_appearance_mode('dark')

bg_image = customtkinter.CTkImage(light_image=Image.open('C:/Users/Lenovo/OneDrive/Desktop/PiSy AI/images/logo.png'), 
                                  dark_image=Image.open('C:/Users/Lenovo/OneDrive/Desktop/PiSy AI/images/logo.png'), 
                                  size=(200, 200))

bg_label = customtkinter.CTkLabel(root, 
                                  text="", 
                                  image=bg_image)
bg_label.pack()

audio_thread = threading.Thread(target=commandLine, 
                                daemon=True)
audio_thread.start()

def quit_window(icon, item):
   icon.stop()
   root.destroy()

def show_window(icon, item):
   icon.stop()
   root.after(0,root.deiconify())

def hide_window():
   root.withdraw()
   image=Image.open("C:/Users/Lenovo/OneDrive/Desktop/PiSy AI/images/logo.png")
   menu=(item('Show', show_window), item('Quit', quit_window))
   icon=pystray.Icon("name", image, "My System Tray Icon", menu)
   icon.run()

root.protocol('WM_DELETE_WINDOW', hide_window)

root.mainloop()
