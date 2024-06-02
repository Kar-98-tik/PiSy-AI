import speech_recognition as sr
import pyautogui
import time

def type_with_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        pyautogui.typewrite(command)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass

if __name__ == "__main__":
    while True:
        type_with_voice()
        time.sleep(1)  # Add a delay to prevent continuous typing, adjust as needed
