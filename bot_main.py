import telebot
from openai import OpenAI

# A function for generating a response from the Open air model
def generate_text(prompt):
    try:
        # Initializing the Openal API client
        client = OpenAI(api_key='API_KEY_OpenAI')
        # Getting a response from the model
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Defining a model for text generation
            messages=[
                {
                    "role": "system",
                    "content": ""
                },
                {"role": "user", "content": prompt}
            ],
        )

        try:
            return float(response.choices[0].message.content)
        except ValueError:
            return response.choices[0].message.content
    except Exception as e:
        return str(e)

# Telegram Bot Initialization
bot = telebot.TeleBot('API_KEY_TeleBot')

# The handler of the start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Hi,{message.from_user.first_name} {message.from_user.last_name}!")

# Text Message Handler
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = generate_text(message.text)
    bot.send_message(message.chat.id, response)

bot.polling()

