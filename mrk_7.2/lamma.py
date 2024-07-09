from llama_index.llms.llama_api import LlamaAPI

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
                history_data = file.readlines()
                messages = [eval(line.strip()) for line in history_data if line.strip()]
            return messages
        except FileNotFoundError:
            return [] # Return an empty list if no history file exists

    def save_history(self):
        with open(self.history_file, 'w') as file:
            for message in self.messages:
                file.write(str(message) + '\n')

    def add_system_message(self):
        system_message = {
            "role": "system",
            "content": "hi i am assistant"
        }
        if not any(msg["role"] == "system" for msg in self.messages):
            self.messages.append(system_message)  # Add system message only if not already present

    def get_llama_response(self, user_message):
        """Generate a response using the OpenAI API with conversation history."""
        self.messages.append({"role": "user", "content": user_message})
        try:
            response = llm.complete(user_message)
            ai_message = response
            self.messages.append({"role": "assistant", "content": ai_message})
            self.save_history()  # Save history after each response
            return response
        except Exception as e:
            print("An error occurred:", e)
            return None

    def main_loop(self):
        self.add_system_message()
        while True:
            query: str = input("user:- ")
            query= query.lower()
            if query == "hi":
                print(" code is working ")
            else :
                response = self.get_llama_response(query)
                print(response)


if __name__ == "__main__":

    while True:
        chatbot = Chatbot()
        chatbot.main_loop()


