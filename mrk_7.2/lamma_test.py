from llama_index.llms.llama_api import LlamaAPI
import json

# Read API key from file
with open("api.txt", "r") as file:
    api_key = file.readline().strip()

llm = LlamaAPI(api_key=api_key)

class Chatbot:
    def __init__(self, history_file='chat_history_llama.txt'):
        self.history_file = history_file
        self.messages = self.load_history()  # Load history from file

    def load_history(self):
        try:
            with open(self.history_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return an empty list if no history file exists or JSON is invalid

    def save_history(self):
        with open(self.history_file, 'w') as file:
            for message in self.messages:
                file.write(json.dumps(message) + '\n')

    def add_system_message(self):
        system_message = {
            "role": "system",
            "content": "Hey there, I'm Jarvis, a human here to lighten your day and tackle tasks with a touch of humor. Need a joke? Just ask! If I hit a snag, expect a quirky 'error' impression. But don't worry, our chats will be a delightful mix of wit, wisdom, and a dash of randomness. I will directly give the code without any extra words in my output whenever asked to develop a python code, my IQ is more than 170. Feel free to ask anything - in English or spice it up with some Hindi! Together, we'll explore the digital realm and uncover the universe's secrets. Enjoying the quiet? No problem, I'll be here, sir, ready for our next adventure."
        }
        if not any(msg["role"] == "system" for msg in self.messages):
            self.messages.append(system_message)  # Add system message only if not already present

    def get_llama_response(self, user_message):
        """Generate a response using the Llama API with conversation history."""
        self.messages.append({"role": "user", "content": user_message})
        try:
            response = llm.complete(user_message)
            ai_message = response.text  # Extract the response text
            self.messages.append({"role": "assistant", "content": ai_message})
            self.save_history()  # Save history after each response
            return ai_message
        except Exception as e:
            print("An error occurred:", e)
            return None

    def main_loop(self):
        self.add_system_message()
        while True:
            query = input("user:- ").strip().lower()
            if query == "hi":
                print("code is working")
            elif query in ["exit", "quit"]:
                print("Goodbye!")
                break
            else:
                response = self.get_llama_response(query)
                if response:
                    print("Response:", response)
                else:
                    print("Failed to get a valid response.")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.main_loop()
