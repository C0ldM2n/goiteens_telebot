import telebot
from telebot import types

bot = telebot.TeleBot('6052072835:AAGW8CGANoe2lexM0mm_R5kRCGvXel8xZiM')


@bot.message_handler(commands=['start'])  # start message
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('💯 Пройти опитування')
    btn2 = types.KeyboardButton('💻 Перейти на сайт')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, вітаю 👋. З чим можу допомогти?')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMLZIz0ROIeKV5cHYSaiDWUdIdpFOcAAjgLAAJO5JlLMrFH0tlPjNAvBA',
                     reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(content_types=['text'])  # LINK BUTTON
def on_click(message):
    if message.text == '💻 Перейти на сайт' or 'Перейти на сайт' or 'Сайт' or 'сайт':
        markup = types.InlineKeyboardMarkup()
        linkbutton = types.InlineKeyboardButton('🌐 Перейти на сайт', url='https://www.lifecell.ua/uk/mobilnij-zvyazok'
                                                                         '/taryfy/')
        markup.add(linkbutton)
        bot.send_message(message.chat.id, 'Натисніть нижче ⬇'.format(message.from_user), reply_markup=markup)
    # survey


bot.polling(none_stop=True)  # nonstop working
