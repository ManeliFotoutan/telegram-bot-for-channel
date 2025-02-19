import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

CHANNEL_ID = 'Channel_id'


bot.send_message(CHANNEL_ID, "Hello, this is a test message to the channel!")
