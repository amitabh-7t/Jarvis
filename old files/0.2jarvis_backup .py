from asyncio.streams import open_connection
import os 
import pyttsx3
import speech_recognition as sr
import datetime
# import googlesearch
import wikipedia
import webbrowser
import smtplib
import pywhatkit
import pyjokes
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("at your SERVICE Sir")

    elif hour>=12 and hour<17:
      speak("Good Afternoon Sir")


    else:
        speak("Good Evening sir")
 
    

def takeCommand():
    #it takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amitabht93@gmail.com', 'your-password')
    server.sendmail('amitabht93@gmail.com' , to ,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        # logic
        if 'who is' in query:
            speak('let me search IN DATA BASE about ' + query )
            query = query.replace("who is"  , "")
            results = wikipedia.summary(query, sentences=2)
            speak("INFORMATION COME OUT FROM OUR DATA BASE is " )
            print(results)
            speak(results)

        elif 'what is' in query:
            speak('let me search IN  DATA BASE about ' + query )
            query = query.replace("what is"  , "")
            results = wikipedia.summary(query, sentences=2)
            speak("INFORMATION COME OUT FROM OUR DATA BASE is" )
            print(results)
            speak(results)
            
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song )
            speak('sir')
            pywhatkit.playonyt(song)

        elif"jarvis are you single" in query :
            speak("i am already in a relationship with internet")
            print(speak)

        # # ##??elif'what about weather today' in query:
        #     speak('just a second sir...')
        #     # query = query.replace("forecast", "")
        #     results = weather_forecast.forecast(place = "Patna" , time="02:29:28", date="2020-12-19", forecast="daily")
        #     print(results)
        #     speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube sir!")

        elif 'music' in query:
            os.startfile('C:\\Users\\Amita\\Music\\zgcs.zpl')
            speak('its music time!')

        elif 'good morning jarvis'in query:
            speak ("a very good morning sir")

        elif 'tell me a joke'  in query:
            speak(pyjokes.get_joke())

        elif 'hello jarvis' in query:
           speak("ohh hello sir!")
        
        elif 'i am good' in query:
            speak("it sounds good!")


        elif 'open photos' in query:
            webbrowser.open("https://photos.google.com/")
            speak("showing your preety moments")

        elif 'are you there jarvis' in query:
            speak("At your service sir")
       
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("here it is, sir!")

        elif 'how are you' in query:
            speak("i am good sir , how are you ?")

        elif 'open mailbox'in query:
            webbrowser.open("mail.google.com")
            speak("opening mail box")

        elif 'upload my files jarvis'in query:
            webbrowser.open("https://drive.google.com/drive/my-drive")
            speak("sure sir")

        elif 'who created you' in query:
            speak("Amitabh thakur")
        
        elif 'what can you do' in query:
            speak("Gentle man i can perform any action by your voice command, and the command must be in my setup!")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("opening facebook")

        elif 'good night' in query:
            speak(" goodnight sir!")

        elif 'open messages' in query:
            webbrowser.open("messages.google.com")
            speak("here is your messages")

        elif 'show me whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("your whatsapp chat is here")

       
        elif 'open my website' in query:
            webbrowser.open("https://rnd-department-of-education.business.site/?utm_source=gmb&utm_medium=referral&fbclid=IwAR3HYD6mTJkS8G99lMz2hkAGK-iusoYk2WqvoXhtA36yIfA3U6GNWrUSvwg")
            speak("opening your working desk")

        elif 'thank you' in query:
            speak("my pleasure")

        elif 'meeting' in query:
            webbrowser.open("https://meet.google.com/")
            speak("okay sir!")


        elif 'current time' in query:
            strTime =datetime.datetime.now().strftime("%I:%M:%p")
            speak(f"sir the time is {strTime}")

        elif 'open documents' in query:
            os.startfile('C:\\Users\\Amita\\Documents')

        elif 'open a new tab' in query:
            webbrowser.open_new_tab
            speak("opening new tab")

        elif 'note my words' in query:
             write:(input)

        elif 'quit jarvis 'in query:
            os.system.exit


        elif 'send email to amitabh' in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "amitabht93@gmail.com"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry sir , it is delayed or either not sent")

        
                
    

 