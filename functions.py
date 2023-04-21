import requests

def weather(city = 'Moscow'):
    url = 'https://wttr.in/' + city + '?format=%l:+%c+%C+%t&lang=ru'
    response = requests.get(url)
    return response.text

def curs():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    return response.text

def cursCurMon(curs1):
    vivod = ''
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    if response.status_code != 200:
        return 'Не удалось подключиться к сайту ЦБ, попробуйте ещё раз'
    result = response.text.split('<Valute ID="')
    for i in result:
        if curs1 in i:
            vivod = i[i.find('inal>')+5:i.find('</Nomi')] + ' ' + i[i.find('<Name>')+6:i.find('</Name>')] + ' - ' + i[i.find('<Value>')+7:i.find('</Value>')] + ' русских рублей (RUB)'


    return vivod