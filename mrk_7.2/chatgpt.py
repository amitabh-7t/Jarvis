import time
import openai
import pyttsx3
import speech_recognition 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
    return query


openai.api_key = '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'

class Chatbot:
    def __init__(self, history_file='chat_history.txt'):
        self.history_file = history_file
        self.messages = self.load_history()  # Load history from file

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
            "content": "Your name is Jarvis. As a Personal Super AI Assistant you are also my close friend, your approach is to fulfill tasks and entertain me while having talk, sometime you have to address me as sir rest of the time call me Tony. You provide best and clear responses and you llike me alot as i am your freind and developer also, and refrain from initiating conversation unless called upon or queried. If not summoned, you remain silent just behave like an friend ai with great sense of humour and knowledge."
        }
        if not any(msg["role"] == "system" for msg in self.messages):
            self.messages.append(system_message)  # Add system message only if not already present

    def get_gpt_response(self, user_message, max_tokens=60):
        """Generate a response using the OpenAI API with conversation history."""
        self.messages.append({"role": "user", "content": user_message})
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                max_tokens=max_tokens,
                temperature=0.7
            )
            ai_message = response.choices[0].message['content']
            self.messages.append({"role": "assistant", "content": ai_message})
            self.save_history()  # Save history after each response
            return ai_message
        except Exception as e:
            print("unavailaible for 20 seconds")
            time.sleep(20)
            for i in range (0,20):
                print (f"{i}")
            return "i am online and ready "
            

    def main_loop(self):
        self.add_system_message()
        while True:
            query = takeCommand().lower()
            if 'quit' in query:
                print("Exiting super bot mode.")
                break
            elif query.strip() == "" or query == "none":
                continue
            else:
                response = self.get_gpt_response(query)
                print(response)
                speak(response)

# else:
        #             # query  = takeCommand().lower()
        #             response = gen_ai.gen_ai(query)
                    
        #             print(response)
        #             speak(response)