import telebot
import os
from dotenv import load_dotenv
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

load_dotenv()

API_TOKEN = os.environ.get("API_TOKEN")
if not API_TOKEN:
    raise ValueError("API_TOKEN is not set. Please set it in your environment variables.")

bot = telebot.TeleBot(API_TOKEN)

CHANNEL_ID = "-1002477964914"
CHANNEL_LINK = "https://t.me/+fDdpCYsIGfk4YzZk"

def is_member(message):
    """
    Check if the user is a member of the specified channel.
    """
    user_info = bot.get_chat_member(CHANNEL_ID, message.from_user.id)
    if not user_info.status in ["administrator", "creator", "member"]:
        bot.send_message(message.chat.id, f"Please subscribe to our channel so you can use this bot: [Join Channel]({CHANNEL_LINK})", parse_mode="Markdown")
        return False
    return True

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    """
    Handle incoming messages.
    """
    if is_member(message):
        bot.reply_to(message, "Hello, thanks for joining!")
    else:
        pass

bot.infinity_polling()
