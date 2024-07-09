from speech_synthesis import speak, takeCommand,query
import wikipedia
import webbrowser
import datetime
import pywhatkit
import pyjokes
import os

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

else:
    pass

        


