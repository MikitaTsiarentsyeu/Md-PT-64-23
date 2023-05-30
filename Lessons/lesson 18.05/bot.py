import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'hello'])
def start_message(message):
    bot.send_message(message.chat.id, "hello there!")

@bot.message_handler(commands=['update'])
def update_message(message):
    html = urlopen("https://kurs.onliner.by/")
    soup = BeautifulSoup(html)
    tags = soup.find_all('p', {'class':'value'})

    buy = tags[0].text
    sell = tags[1].text
    
    bot.send_message(message.chat.id, f"buy - {buy}, sell - {sell}")

bot.polling()
