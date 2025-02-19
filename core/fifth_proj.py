import telebot
import feedparser
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.environ.get("API_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")
RSS_FEED_URL = "https://thealibigdeli.ir/blog/feed/rss"  


bot = telebot.TeleBot(API_TOKEN)

LAST_POST_FILE = "last_post_id.txt"

def read_last_post_id():
    if os.path.exists(LAST_POST_FILE):
        with open(LAST_POST_FILE, 'r') as f:
            return f.read().strip()
    return None

def save_last_post_id(post_id):
    with open(LAST_POST_FILE, 'w') as f:
        f.write(post_id)


def check_and_send_post():
    last_post_id = read_last_post_id()
    print(f"Last post ID: {last_post_id}")

    feed = feedparser.parse(RSS_FEED_URL)
    latest_entry = feed.entries[0]
    post_id = latest_entry.id

    print(f"Latest post ID: {post_id}")

    if post_id != last_post_id:
        bot.send_message(CHANNEL_ID, f"آخرین پست: {latest_entry.title}\n\n{latest_entry.link}")
        save_last_post_id(post_id)

def start_bot():
    try:
        while True:
            check_and_send_post()
            time.sleep(600)
    except KeyboardInterrupt:
        print("Bot stopped gracefully.")

if __name__ == "__main__":
    start_bot()
