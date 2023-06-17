import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6071863213:AAEmCqtglY6HbR7_tlkluXa9ZlbcW8alHZk')
gigi = None
mints = None
sms = None
svc = None
hots = None
bud = None


@bot.message_handler(commands=['start'])  # start message
def start(message):
    conn = sqlite3.connect('user_inputs.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS user_inputs (id int auto_increment primary key, gigi varchar(50), '
                'mints varchar(50), sms varchar(50), svc varchar(50), hots varchar(50), bud varchar(50))')

    conn.commit()
    cur.close()
    conn.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('💯 Підібрати тариф')
    btn2 = types.KeyboardButton('💻 Перейти на сайт')

    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, вітаю 👋. З чим можу допомогти?')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMLZIz0ROIeKV5cHYSaiDWUdIdpFOcAAjgLAAJO5JlLMrFH0tlPjNAvBA'
                     .format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])  # LINK BUTTON
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '💻 Перейти на сайт':
            markup = types.InlineKeyboardMarkup()
            linkbutton = types.InlineKeyboardButton('🌐 Перейти на сайт', url='https://www.lifecell.ua/uk/mobilnij'
                                                                             '-zvyazok/taryfy/')
            markup.add(linkbutton)
            bot.send_message(message.chat.id, 'Натисніть нижче ⬇', reply_markup=markup)

        elif message.text == '💯 Підібрати тариф':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            startt = types.KeyboardButton('🚀 Розпочати')
            back = types.KeyboardButton('🔙 Головне меню')
            markup.add(startt, back)

            bot.send_message(message.chat.id, '💯 Підібрати тариф\n\nПісля проходження цього опитування, я запропоную '
                                              'вам декілька тарифів які мають підійти вам.\n\nВи готові почати?',
                             reply_markup=markup)

        elif message.text == '🔙 Головне меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('💯 Підібрати тариф')
            btn2 = types.KeyboardButton('💻 Перейти на сайт')
            markup.add(btn1, btn2)

            bot.send_message(message.chat.id, '🔙 Головне меню', reply_markup=markup)

        # survey

        elif message.text == '🚀 Розпочати':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bt1 = types.KeyboardButton('<10 Гб')
            bt2 = types.KeyboardButton('>10 Гб')
            back = types.KeyboardButton('🔙 Головне меню')
            markup.add(bt1, bt2, back)

            bot.send_message(message.chat.id, '🚀 Початок підбору', reply_markup=markup)
            bot.send_message(message.chat.id, 'Який обсяг мобільного інтернету вам зазвичай потрібен на місяць?', )
            bot.register_next_step_handler(message, user_gigi)


@bot.message_handler(content_types=['text'])
def user_gigi(message):
    global gigi
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('<1000 Хвилин')
    bt2 = types.KeyboardButton('>1000 Хвилин')
    back = types.KeyboardButton('🔙 Головне меню')
    markup.add(bt1, bt2, back)

    gigi = message.text.strip()
    bot.send_message(message.chat.id, 'Яку кількість хвилин розмови на місяць ви зазвичай використовуєте?')
    bot.register_next_step_handler(message, user_mints)


def user_mints(message):
    global mints
    mints = message.text.strip()
    bot.send_message(message.chat.id, 'Введите sms')
    bot.register_next_step_handler(message, user_sms)


def user_sms(message):
    global sms
    sms = message.text.strip()
    bot.send_message(message.chat.id, 'Введите service')
    bot.register_next_step_handler(message, user_svc)


def user_svc(message):
    global svc
    svc = message.text.strip()
    bot.send_message(message.chat.id, 'Введите hotspot')
    bot.register_next_step_handler(message, user_hots)


def user_hots(message):
    global hots
    hots = message.text.strip()
    bot.send_message(message.chat.id, 'Введите Budget')
    bot.register_next_step_handler(message, user_bud)


def user_bud(message):
    bud = message.text.strip()

    conn = sqlite3.connect('user_inputs.sql')
    cur = conn.cursor()
    # global = импорт в других переменных в сообщение и перевод их в базу данных
    cur.execute(
        "INSERT INTO user_inputs (gigi, mints, sms, svc, hots, bud) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
            gigi, mints, sms, svc, hots, bud))
    conn.commit()
    cur.close()
    conn.close()

    # Предложение посмотреть все данные из БД (чем то надо заменить)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Tarifo fil', callback_data='user_inputs'))
    bot.send_message(message.chat.id, 'Polzovatel geniy', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('user_inputs.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM user_inputs')
    user_inputs = cur.fetchall()

    info = ''
    for el in user_inputs:
        info += f'Gigs: {el[1]}, Minutes: {el[2]}, SMS: {el[3]}, Service: {el[4]}, hotspot: {el[5]}, Budget: {el[6]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)  # nonstop working
