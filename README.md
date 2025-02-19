# Telegram Bot for Channel Management and RSS Feed Updates

This project involves creating a Telegram bot that interacts with a specified channel, sends messages, and fetches the latest RSS feed posts periodically. The bot also checks if users are members of the channel before allowing them to interact with the bot.

### Features:
1. **Sending Messages to a Channel:**
   - The bot can send messages to a specified channel using the provided `CHANNEL_ID`.

2. **RSS Feed Fetcher:**
   - Every 10 minutes, the bot fetches the latest post from a given RSS feed URL and posts it to the channel.
   - Duplicate posts are prevented by checking the uniqueness of each post.

3. **Channel Membership Check:**
   - Before responding to a user, the bot checks if they are a member of the specified channel.
   - If not a member, the bot sends a message to ask the user to join the channel.

---

### Prerequisites:
- Python 3.x
- `telebot` library
- `dotenv` library
- An active Telegram bot token (use [BotFather](https://core.telegram.org/bots#botfather) to create your bot)
- A Telegram channel where the bot can post messages
- Access to an RSS feed URL for periodic updates

### Setup:
1. **Clone the Repository:**

2. **Install Dependencies:**
   Make sure you have `telebot` and `dotenv` installed:
   ```bash
   pip install pyTelegramBotAPI python-dotenv
   ```

3. **Environment Variables:**
   Create a `.env` file in the root directory and add your API token:
   ```
   API_TOKEN=your_telegram_bot_token
   ```

4. **Run the Bot:**
   Run the bot script to start polling and interact with the Telegram channel:
   ```bash
   python first_join_then_use.py
   ```

---

### Code Explanation:

#### **first_join_then_use.py**
This script handles user interaction and ensures that only members of the specified channel can use the bot.

- **is_member(message)**: Checks if a user is a member of the channel.
- **message_handler(message)**: Handles incoming messages and responds accordingly.

#### **fifth_proj.py**
This script fetches the latest RSS feed post every 10 minutes and sends it to the Telegram channel, ensuring that no duplicate posts are shared.

- **RSS Feed URLs**: You can use any of the following URLs:
   - `https://thealibigdeli.ir/blog/feed/rss`
   - `https://www.varzesh3.com/rss/list`

---

### Important Notes:
- Ensure that your bot has permission to send messages to the channel.
- For scheduling periodic tasks, you can use a task scheduler like `cron` on Unix-based systems or a scheduling library like `APScheduler` in Python.
- The bot checks for duplicate posts to avoid spamming the channel.
