import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/last/good/'
API_KEY = '6197809958:AAElbdY6Pn-oYwa1DUx8mX6KCCORT3xZbG0'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return[c.text for c in anekdots]

jokes = parser(URL)
random.shuffle(jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Салам! Чтобы произошла разрывная введи любую цифру: ')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, jokes[0])
        del jokes[0]
    else:
       bot.send_message(message.chat.id, 'Введи любую цифру: ')

bot.polling()

