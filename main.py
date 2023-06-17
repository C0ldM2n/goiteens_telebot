import telebot

bot = telebot.TeleBot('6052072835:AAGW8CGANoe2lexM0mm_R5kRCGvXel8xZiM')  # use token from config for token


@bot.message_handler(commands=['start'])  # start message
def main(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, вітаю u"\". З чим можу допомогти?')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMLZIz0ROIeKV5cHYSaiDWUdIdpFOcAAjgLAAJO5JlLMrFH0tlPjNAvBA')


bot.polling(none_stop=True) # nonstop working
