import telebot
import functions



token = "5591651962:AAGxXHAhVw3q5iG-Kq_JCZpxTr6aThLwQL8"
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
    vivod = ''
    if len(queue) == 1:
        vivod = functions.curs()
    elif len(queue) == 2:
        vivod = functions.cursCurMon(queue[1])
    else:
        vivod = 'Неправильно введён запрос'
    bot.send_message(message.chat.id,vivod)




bot.infinity_polling()