import requests
from lxml import etree

def weather(city = 'Moscow'):
    url = 'https://wttr.in/' + city + '?format=%l:+%c+%C+%t&lang=ru'
    response = requests.get(url)
    return response.text

def curs():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url).text
    response = response.replace('<?xml version="1.0" encoding="windows-1251"?>','')
    SiteXml = etree.fromstring(response)
    result = ''
    for i in SiteXml.getchildren():
        temp = i.getchildren()
        result += temp[2].text + ' ' + temp[-2].text + ' (' + temp[1].text + ') - ' + temp[-1].text + ' Русских Рублей (RUB)\n'
    return(result)

def cursCurMon(currentCurs):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url).text
    response = response.replace('<?xml version="1.0" encoding="windows-1251"?>', '')
    SiteXml = etree.fromstring(response)
    result = ''
    for i in SiteXml.getchildren():
        temp = i.getchildren()
        if temp[1].text == currentCurs:
            result = temp[2].text + ' ' + temp[-2].text + ' (' + temp[1].text + ') - ' + temp[-1].text + ' Русских Рублей (RUB)\n'
    if result == '':
        result = 'Неверный код валюты'
    return result