import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get("BOT_TOKEN", "YOUR_TOKEN_HERE")
bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🎰 Omadni sinab ko'r", url="https://quiz-bot-brown-tau.vercel.app/bugun-omading-bormi.html")
    )
    markup.row(
        InlineKeyboardButton("🧠 Viktorina", url="https://quiz-bot-brown-tau.vercel.app/index.html")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"Salom, {name}! 👋\n\n"
        f"Quyidagi o'yinlardan birini tanlang:\n\n"
        f"🎰 *Omad G'ildiragi* — omadingizni sinab ko'ring!\n"
        f"🧠 *Viktorina* — bilimingizni tekshiring!",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(
        message.chat.id,
        "🎮 O'yinlar menyusi:",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(
        message.chat.id,
        "O'yin tanlang 👇",
        reply_markup=main_menu()
    )

print("Bot ishga tushdi! ✅")
bot.infinity_polling()
