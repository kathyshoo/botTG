import telebot
import functions



token = "5591651962:AAFtI8BFgkbsmr0iIFy8h7moAAoU2zyYAgo"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def welc(message):
    bot.send_message(message.chat.id, "Привет:) Я Нася, а ещё я ботик) Ну... как вы - люди, меня зовёте🤔 Но ничего) Я не обижаюсь. Могу я как-то тебе помочь?)\n"
                                      "Пока, что я умею только:\n"
                                      "• Определять погоду в заданном городе (чтобы задать город введи /weather *нужный город*)\n"
                                      "• Узнавать все курсы валют с сайта ЦБ) экономист😎 /money или /money USD чтобы узнать курс определённой валюты к рублю\n"
                                      "прости, что разочаровала(( Но я научусь большему!! ОБЕЩАЮ!")

@bot.message_handler(commands=['weather'])
def welc(message):
    mas = message.text.split(' ')
    bot.send_message(message.chat.id, functions.weather(mas[1]))

@bot.message_handler(commands=['money'])
def welc(message):
    queue = message.text.split(' ')
    if len(queue) == 1:
        mas = functions.curs().split('<Valute ID=')
        masv = []
        for i in mas:
            if i[1] != '?':
                temp = i.split('</')
                masv.append(temp[2][temp[2].index('al>')+3:] + ' ' + temp[3][temp[3].index('me>')+3:] + ' (' + temp[1][-3:] + ')' + ' - ' + temp[4][temp[4].index('ue>')+3:] + ' рублей (₽)')
        vivod = ''
        for k in masv:
            vivod += k + '\n'
    elif len(queue) == 2:
        vivod = functions.cursCurMon(queue[1])
        if vivod == '':
            vivod = 'Неправильно введена команда'
    else:
        vivod = 'Неправильно введён запрос'

    bot.send_message(message.chat.id,vivod)




bot.infinity_polling()