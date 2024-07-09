# # Import the Python SDK
# import google.generativeai as genai
# # Used to securely store your API key


# GOOGLE_API_KEY=userdata.get('AIzaSyAXOQF8JodMbG8ssxUN94g-hfGVCPaK75M')
# genai.configure(api_key=GOOGLE_API_KEY)

# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

import google.generativeai as genai
import os

genai.configure(api_key=os.environ["AIzaSyAXOQF8JodMbG8ssxUN94g-hfGVCPaK75M"])

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Write a story about a AI and magic")
print(response.text)