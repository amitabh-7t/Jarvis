import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "browser":"msedge",
    "Mail":"OUTLOOK",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vs code": "code",
    "powerpoint": "powerpnt",
    "github": "github",
    "microsoft store": "ms-windows-store",
    "telegram": "telegram",
    "whatsapp": "whatsapp",
    "skype": "skype",
    "spotify": "spotify",
    "notepad": "notepad",
    "photoshop": "photoshop",
    "calculator": "calc",
    "discord": "discord",
    "outlook": "outlook",
    "zoom": "zoom",
    "linkedin": "linkedin",
    "facebook": "facebook",
    "twitter": "twitter",
    "instagram": "instagram",
    "reddit": "reddit",
    "snapchat": "snapchat",
    "twitch": "twitch",
    "youtube": "youtube"
}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("firday","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing  , sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak(" closed last tab sir")
    elif "two tabs" in query:
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("closed 2 tabs")
    elif "three tabs" in query:
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("closed 3 tabs")
        
    elif "four tabs" in query:
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("closed 4 tabs sir")
    elif "five tabs" in query:
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        # sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("closed 5 tabs")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
