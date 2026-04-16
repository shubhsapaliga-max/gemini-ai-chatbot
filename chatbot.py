from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("AI Chatbot Started (type 'exit' to stop)\n")

# Store conversation history
chat_history = ""

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    # Add user message to history
    chat_history += f"You: {user_input}\n"

    try:
        # Send conversation to Gemini
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=chat_history
        )

        bot_reply = response.text

        print("Bot:", bot_reply)

        # Add bot reply to history
        chat_history += f"Bot: {bot_reply}\n"

    except Exception as e:
        print("Error:", e)