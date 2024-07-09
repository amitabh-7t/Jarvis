import os 
import pyttsx3
import vobject
import speech_recognition as sr
import datetime
import pyautogui
import webbrowser
import pywhatkit
import speedtest
import pyjokes
import pyautogui
import requests
from bs4 import BeautifulSoup
import openai
openai.api_key = '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' 
import openai 
import gen_ai
import time
from llama_index.llms.llama_api import LlamaAPI
api_key = "LL-njIR0xcZUjVmfA5m7BPEO9SUBRaxcysf2DQzJIeuvEGFdynsrtjqRcE5MmpqoHX4"
llm = LlamaAPI(api_key=api_key)

class Chatbot:
    def __init__(self, history_file='chat_history.txt', api_key=api_key):
        self.history_file = history_file
        self.messages = self.load_history()  # Load history from file
        self.api_key = api_key
        self.llama_api_endpoint = 'http://localhost:5000/llama'  # Default or local endpoint

    def load_history(self):
        """Load chat history from a file."""
        try:
            with open(self.history_file, 'r') as file:
                history_data = file.readlines()
                messages = [eval(line.strip()) for line in history_data if line.strip()]
            return messages
        except FileNotFoundError:
            return []  # Return an empty list if no history file exists

    def save_history(self):
        """Save the current chat history to a file."""
        with open(self.history_file, 'w') as file:
            for message in self.messages:
                file.write(str(message) + '\n')

    def add_system_message(self):
        """Adds a system-level initialization message to set the context for the conversation."""
        system_message = {
            "role": "system",
            "content": "Hey there, I'm your AI assistant, ready to help with your queries."
        }
        self.messages.append(system_message)

    def chat(self, user_message):
        """Process a user message through the Llama AI model and handle the conversation."""
        self.messages.append({"role": "user", "content": user_message})
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(self.llama_api_endpoint, json={"messages": self.messages}, headers=headers)
        if response.status_code == 200:
            response_content = response.json()['response']
            self.messages.append({"role": "assistant", "content": response_content})
            self.save_history()
            return response_content
        else:
            return "Error processing your message, please try again later."
    def create_python_file(filename, code):
        try:
            with open(filename, 'w') as file:
                file.write(code)
            print(f"Python file '{filename}' created successfully.")
        except Exception as e:
            print(f"Error occurred while creating the file: {e}")

    def gemini(query):
        speak("connected to gemini")
        query = takeCommand.lower()
        if "yes" in query :
            speak("okay sir , feel free to ask ")
            query = takeCommand.lower()
            response = gen_ai.gen_ai(query)
            print(response)
            speak(response)
        elif("switch to jarvis mode"):
            speak(" disconnected from google AI sir") 
            return
        elif "search for" in query :
            query.replace("search for","")
            response = gen_ai.gen_ai(query)
            print(response)
            speak(response)
        elif("exit from this mode "):
            speak(" disconnected from google AI sir") 
            return

    def main_loop(self):
        self.add_system_message()
        is_music_playing = False 
        while True:
            query = takeCommand().lower()
            if 'quit' in query:
                print("Exiting super bot mode.")
                break
            elif query.strip() == "" or query == "none":
                continue
            
            elif "open" in query :
                from Dictapp import openappweb
                openappweb(query)

            elif "close" in query :
                from Dictapp import closeappweb
                closeappweb(query)

            elif "go to sleep" in query or 'OK great thank you go to sleep now' in query:
                speak("okay sir")
                while True:
                    query=takeCommand().lower()
                    
                    if query == "wake up jarvis"  or query == "daddy's home" :
                        speak("at your service sir")
                        return
        
                    else:
                        continue

            elif "connect to gemini" in query :
                while True:
                    speak("connected to gemini")
                    query=takeCommand().lower()
                    
                    response = gen_ai.gen_ai(query)
                    print(response)
                    speak(response)
    
                    if"switch to jarvis mode" in query:
                        speak("we are now offline and ready")
                        return

            elif 'search for' in query :
                speak("okay!")
                results = webbrowser.open("https://www.google.com/search?q="+ query.replace("search for"  , ""))  

            elif 'play' in query or "jarvis play " in query:
                song = query.replace('play', '') or query.replace('jarvis play','') 
                speak('playing' + song )
                pywhatkit.playonyt(song)

            elif 'tell me a joke' in query:
                speak(pyjokes.get_joke())

            elif 'show me photos'in query or "show my photos" in query :
                webbrowser.open("https://photos.google.com/")
                speak("showing your preety moments")

            elif  query == 'open google' :
                webbrowser.open("google.com")
                speak("opening google, sir!")

            elif "like this song" in query or "like song" in query:
                speak("Liking Song")
                exec(open(r"C:\jarvis\MRK6\5_6\likeSong.py").read())
                
            elif "give me the number of " in query:
                name_to_search = query.replace("give me the number of ", "").strip()
                vcf_file = 'contacts1.csv'
                number = Chatbot.search_number_in_vcf(vcf_file, name_to_search)
                print(f"Number for {name_to_search}: {number}")


            elif "start music" in query:
                speak("opening music")
                exec(open(r"C:\jarvis\MRK6\5_6\openAndPlay.py").read())

            elif "pause music" in query or "pause song" in query or "play music" in query or "resume music" in query:
                exec(open(r"C:\jarvis\MRK6\5_6\pausePlayMusic.py").read())
                        
            elif 'open cloud storage'in query:
                webbrowser.open("https://drive.google.com/drive/my-drive")
                speak("sure sir")

            elif query == 'who created you':
                speak("Amitabh thakur")

            elif 'pause' in query:
                if is_music_playing:
                    pywhatkit.pause_playback()  # Pause the music
                    speak("Music paused")
                    is_music_playing = False 

            elif 'resume' in query or 'play' in query:
                if not is_music_playing:
                    pywhatkit.resume_playback()  # Resume the music
                    speak("Resuming music")
                    is_music_playing = True

            elif "mute" in query :
                pyautogui.press("m")
                speak("video muted")

            elif "click my photo" in query :
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                speak("SMILE")
                pyautogui.press("enter")

            elif "play a game" in query :
                from game import game_play
                game_play()

            elif "translate" in query :
                import translator
                from translator import translategl
                query = query.replace("","")
                query = query.replace("translate","")
                translategl(query)

            elif 'open messages' in query :
                webbrowser.open("messages.google.com")
                speak("here is your messages")

            elif 'show me whatsapp' in query :
                webbrowser.open("https://web.whatsapp.com/")
                speak("your whatsapp chat is here")

            elif 'temperature'in query :
                search = "temperature in bangalore  "
                url= f"https://www.google.com/search?q={search}"
                r= requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_ ="BNeawe").text
                speak(f"current{search}is {temp}")

            elif "today's weather" in query:
                search = "weather in bangalore  "
                url= f"https://www.google.com/search?q={search}"
                r= requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_ ="BNeawe").text
                speak(f"current{search}is {temp}")

            elif query == 'weather':
                speak("which place sir ?")
                query=takeCommand.lower()
                search = f"weather at {query}"
                url= f"https://www.google.com/search?q={search}"
                r= requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_ ="BNeawe").text
                speak(f"Current{search} is {temp} Sir!")                

            elif 'start a meeting' in query :
                webbrowser.open("https://meet.google.com/")
                speak("okay Sir!")

            elif 'current time'in query :
                strTime =datetime.datetime.now().strftime("%I:%M:%p")
                speak(f"sir the time is {strTime}")

            elif 'open documents' in query :
                os.startfile('C:\\Users\\Amita\\Documents')

            elif 'quit' in query:
                os.system.exit

            elif "shutdown the system" in query :
                speak("Are You sure you want to shutdown")
                query = takeCommand.lower() #input("Do you wish to shutdown your computer? (yes/no)")
                if query == "yes":
                        os.system("shutdown /s /t 1")
                elif query == "no":
                        break
                
            elif "screenshot" in query :
                import pyautogui 
                im = pyautogui.screenshot()
                im.save("ss.jpg")
            
            elif  "internet speed" in query :
                wifi  = speedtest()
                upload_net = wifi.upload()/1048576         
                download_net = wifi.download()/1048576
                print("Wifi Upload Speed is", upload_net)
                print("Wifi download speed is ",download_net)
                speak(f"Wifi download speed is {download_net}")
                speak(f"Wifi Upload speed is {upload_net}")

            elif "jarvis connect to gemini " in query :
                Chatbot.gemini()
            elif "jarvis write a python code" in query or "write a python code" in query or "write a code " in query:
                print("generating code")
                response = self.get_gpt_response(query)
                if  response:
                    topic = query.replace(" write a code", "").strip() or query.replace(" write a python code", "").strip()
                    Chatbot.create_python_file(topic, response)
                    speak(f"created code for topic: {topic}")
                else:
                    speak("Sorry, I couldn't generate the code for you.")
                
            else:
                # # resp = llm.complete(query)
                # print(resp)
                # speak(resp)
                print (chatbot.chat(query))
                

            # else:
            #         response = self.get_gpt_response(query)
            #         if response is None or "I don't have real-time information on specific events, sir." in response or "I can't play music, sir. How else may I assist you?" in response or "I can't browse the internet, sir." in response or "I can't provide real-time weather updates, sir." in response or "unable to access" in response or "I don't have access to specific news archives, sir." in response or "unavailable" in response:
            #             print (" ...")

            #         else:
            #             print(response)
            #             speak(response)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir! ")
    elif hour>=12 and hour<17:
      speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 700
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        
        audio =r.listen(source)
    try:
        print("Recognizing ....")
        query = r.recognize_google(audio, language='en-in')
        print(f"sir : {query}\n")

    except Exception as e:
        #print(e)
        print(".")
        return "None"
    return query
        
def browswer(query):
    if  'open a new tab' :
            webbrowser.open_new_tab
            speak("opening new tab") 
    elif'close_tab':
        pyautogui.hotkey("ctrl", "w")
    elif'close browser' :
        os.system("taskkill /im msedge.exe /f")

if __name__ == "__main__":        
    # wishMe()
  
    while True:
        
        chatbot = Chatbot()
        chatbot.main_loop()
        


