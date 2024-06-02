import speech_recognition as sr
import pyttsx3
import threading
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_wake_word(recognizer, microphone):
    with microphone as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        wake_word = recognizer.recognize_google(audio).lower()
        if "listen pc" in wake_word:
            return True
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return False

def listen_for_commands(recognizer, microphone):
    with microphone as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Command:", command)

        if "open application" in command:
            speak("Which application would you like to open?")
            application_name = input("Enter application name: ").lower()
            open_application(application_name)
        # Add more command handling logic here

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def open_application(application_name):
    if "notepad" in application_name:
        os.system("notepad")
    elif "calculator" in application_name:
        os.system("calc")
    elif "web browser" in application_name:
        os.system("start chrome")  # Modify this line based on your default web browser
    else:
        speak(f"Sorry, I don't know how to open {application_name}")

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    speak("Hello! I'm your virtual assistant. Say 'Listen PC' to activate me.")

    while True:
        if listen_wake_word(recognizer, microphone):
            speak("How can I assist you?")
            command_thread = threading.Thread(target=listen_for_commands, args=(recognizer, microphone))
            command_thread.start()
            command_thread.join()  # Wait for the command thread to finish before looping again

if __name__ == "__main__":
    main()
