import telebot
from telebot import types
import text

bot = telebot.TeleBot('6109820425:AAH-yMur4m_EeHufvwl0OuZZzBy7hgwMHsE')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Рассказать', callback_data='tell')
    btn2 = types.InlineKeyboardButton('Меню', callback_data='menu')
    btn3 = types.InlineKeyboardButton('Помощь психолога',callback_data='ps')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
                   caption=f"Привет, {message.from_user.first_name}!\nЯ, помощник Анастасии, чат-бот по отношениям 🙌\n\nДавай я расскажу тебе чем мы будем тут заниматься?",
                   reply_markup=markup)



# @bot.message_handler()
# def none(message):
#     if message != 'Start' and message != "menu" and message != "PS":
#         bot.send_message(message.chat.id, f'Сообщение не распознано - такой команды не существует 🤨')


def tell(message):
    markup = types.InlineKeyboardMarkup()
    btn4 = types.InlineKeyboardButton('Познакомится', callback_data='about')
    btn5 = types.InlineKeyboardButton('Дальше', callback_data='next')
    markup.row(btn4)
    markup.row(btn5)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
                   caption=text.tell,
                   reply_markup=markup)

def about(message):
    markup = types.InlineKeyboardMarkup()
    naz = types.InlineKeyboardButton('Назад', callback_data='tell')
    markup.row(naz)
    file = open('./meet1.jpg', 'rb')
    file1 = open('./meet2.jpg', 'rb')
    bot.send_message(message.chat.id, text.tell)
    bot.send_photo(message.chat.id, file)
    bot.send_photo(message.chat.id, file1,reply_markup=markup)

def next(message):
    markup = types.InlineKeyboardMarkup()
    btn6 = types.InlineKeyboardButton('Давай', callback_data='go')
    nazaddd = types.InlineKeyboardButton('Назад', callback_data='tell')
    markup.row(btn6)
    markup.row(nazaddd)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
                   caption=text.next, reply_markup=markup)

def go(message):
    markup = types.InlineKeyboardMarkup()
    textt = types.InlineKeyboardButton('Давай', callback_data='goo')
    naza = types.InlineKeyboardButton('Назад', callback_data='next')
    markup.row(textt)
    markup.row(naza)
    file = open('./yes.jpg', 'rb')
    #bot.delete_message(message.chat.id, message.message_id)
    bot.send_photo(message.chat.id, file,
                   caption=text.ok, reply_markup=markup)
def goo(message):
    markup = types.InlineKeyboardMarkup()
    dawai1 = types.InlineKeyboardButton('Давай', callback_data='gooo')
    nazad = types.InlineKeyboardButton('Назад', callback_data='goo')
    markup.row(dawai1)
    markup.row(nazad)
    file = open('./yes.jpg', 'rb')
    #bot.delete_message(message.chat.id, message.message_id)
    bot.send_photo(message.chat.id, file,
                   caption=text.dawai1, reply_markup=markup)

def gooo(message):
    markup = types.InlineKeyboardMarkup()
    dawai2 = types.InlineKeyboardButton('Давай', callback_data='goooo')
    nazadd = types.InlineKeyboardButton('Назад', callback_data='goo')
    markup.row(dawai2)
    markup.row(nazadd)
    file = open('./yes.jpg', 'rb')
    #bot.delete_message(message.chat.id, message.message_id)
    bot.send_photo(message.chat.id, file,
                   caption=text.dawai2, reply_markup=markup)

def goooo(message):
    markup = types.InlineKeyboardMarkup()
    btnzap = types.InlineKeyboardButton('Запись на консультацию', callback_data='ps')
    btnex = types.InlineKeyboardButton('Выход в меню', callback_data='menu')
    markup.row(btnzap)
    markup.row(btnex)
    #bot.delete_message(message.chat.id, message.message_id)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
                   caption=text.dawai3, reply_markup=markup)

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup()
    btn7 = types.InlineKeyboardButton('Отношения', callback_data="otnoshenia")
    btn8 = types.InlineKeyboardButton('Упражения и техники', callback_data="ypr")
    btn9 = types.InlineKeyboardButton('Психологические тесты',callback_data="tests")
    btn10 = types.InlineKeyboardButton('Полезные видео', callback_data="video")
    btn11 = types.InlineKeyboardButton('Полезные книги', callback_data="books")
    ps = types.InlineKeyboardButton('Связаться с психологом', callback_data="ps")
    markup.row(btn7)
    markup.row(btn8)
    markup.row(btn9)
    markup.row(btn10)
    markup.row(btn11)
    markup.row(ps)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
                   caption=text.menu, reply_markup=markup)

def otnoshenia(message):
    markup = types.InlineKeyboardMarkup()
    otnoshenia = types.InlineKeyboardButton('Давай', callback_data="otn1")
    markup.row(otnoshenia)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.otnoshenia, reply_markup=markup)

def otn1(message):
    markup = types.InlineKeyboardMarkup()
    otn1 = types.InlineKeyboardButton('Далее', callback_data="stad")
    markup.row(otn1)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.stadii, reply_markup=markup)

def stad(message):
    markup = types.InlineKeyboardMarkup()
    stad = types.InlineKeyboardButton('Далее', callback_data="why")
    markup.row(stad)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.why, reply_markup=markup)

def why(message):
    markup = types.InlineKeyboardMarkup()
    why = types.InlineKeyboardButton('Далее', callback_data="why1")
    markup.row(why)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.why1, reply_markup=markup)

def why1(message):
    markup = types.InlineKeyboardMarkup()
    exi = types.InlineKeyboardButton('Выйти из отношений', callback_data="exi")
    save = types.InlineKeyboardButton('Сохранить отношения', callback_data="save")
    markup.row(exi)
    markup.row(save)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.why2, reply_markup=markup)

def exi(message):
    markup = types.InlineKeyboardMarkup()
    exitt = types.InlineKeyboardButton('Связатся с психологом', callback_data="ps")
    markup.row(exitt)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.exi, reply_markup=markup)

@bot.message_handler(commands=['ps'])
def ps(message):
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.call)

def save(message):
    markup = types.InlineKeyboardMarkup()
    zvon = types.InlineKeyboardButton('Связатся с психологом', callback_data="ps")
    markup.row(zvon)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.save, reply_markup=markup)

def ypr(message):
    markup = types.InlineKeyboardMarkup()
    ypr1 = types.InlineKeyboardButton('Упражнение 1', callback_data="ypr1")
    ypr2 = types.InlineKeyboardButton('Упражнение 2', callback_data="ypr2")
    texn1 = types.InlineKeyboardButton('Техника 1', callback_data="texn1")
    texn2 = types.InlineKeyboardButton('Техника 2', callback_data="texn2")
    markup.row(ypr1, texn1)
    markup.row(ypr2, texn2)
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.ypr, reply_markup=markup)

def ypr1(message):
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.ypr1)

def ypr2(message):
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.ypr2)

def texn1(message):
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.texn1)

def texn2(message):
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.texn2)

def books(message):
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.books)

def tests(message):
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.tests)

def video(message):
    file = open('./yes.jpg', 'rb')
    bot.send_photo(message.chat.id, file,
    caption=text.video)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'tell':
        tell(callback.message)
    elif callback.data == 'next':
        next(callback.message)
    elif callback.data == 'menu':
        menu(callback.message)
    elif callback.data == 'tests':
        tests(callback.message)
    elif callback.data == 'go':
        go(callback.message)
    elif callback.data == 'goo':
        goo(callback.message)
    elif callback.data == 'gooo':
        gooo(callback.message)
    elif callback.data == 'goooo':
        goooo(callback.message)
    elif callback.data == 'otnoshenia':
        otnoshenia(callback.message)
    elif callback.data == 'otn1':
        otn1(callback.message)
    elif callback.data == 'stad':
        stad(callback.message)
    elif callback.data == 'why':
        why(callback.message)
    elif callback.data == 'why1':
        why1(callback.message)
    elif callback.data == 'exi':
        exi(callback.message)
    elif callback.data == 'ps':
        ps(callback.message)
    elif callback.data == 'save':
        save(callback.message)
    elif callback.data == 'ypr':
        ypr(callback.message)
    elif callback.data == 'ypr1':
        ypr1(callback.message)
    elif callback.data == 'ypr2':
        ypr2(callback.message)
    elif callback.data == 'texn1':
        texn1(callback.message)
    elif callback.data == 'texn2':
        texn2(callback.message)
    elif callback.data == 'video':
        video(callback.message)
    elif callback.data == 'books':
        books(callback.message)
    elif callback.data == 'about':
        about(callback.message)

bot.polling(none_stop=True)