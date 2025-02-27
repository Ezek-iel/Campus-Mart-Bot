from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()

bot = TeleBot(os.getenv("BOT_API_TOKEN"))


@bot.message_handler(commands=["start"])
def start(message):

    welcome_message = """
    Hey there! Looking for snacks, supplies, or services on campus? This bot connects you directly to Covenant University's sellers. Easily browse   their listings and get in touch. Tap to get started!
    """
    bot.send_message(message.chat.id, welcome_message)


bot.infinity_polling()
