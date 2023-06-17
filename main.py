import telebot
from telebot import types
import json
import functions as fu

with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

bot = telebot.TeleBot(config['token'])


@bot.message_handler(commands=['start'])
def handle_start(message):
    # Отправка приветственного сообщения
    bot.reply_to(message, "Привет, я бот!")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Ваша логика обработки сообщения
    response = process_message(message.text)

    if response is None:
        # Ответить, если бот не смог понять сообщение
        bot.reply_to(message, "Извините, я не понимаю ваше сообщение.")
    else:
        # Ответить с обработанным сообщением
        bot.reply_to(message, response)

def process_message(text):
    # Здесь вы можете добавить свою собственную логику обработки сообщений
    # и возвратить обработанное сообщение или None, если бот не понял

    return None


bot.polling()
