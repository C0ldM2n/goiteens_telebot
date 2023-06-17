import telebot
import json

with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

bot = telebot.TeleBot(config['token'])


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, вітаю. З чим можу допомогти?')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMLZIz0ROIeKV5cHYSaiDWUdIdpFOcAAjgLAAJO5JlLMrFH0tlPjNAvBA')


bot.polling(none_stop=True)
