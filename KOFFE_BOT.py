import telebot
import random
import requests
import bs4


bot = telebot.TeleBot('1191763095:AAE2k6V96eDJiFQUrhdF9KHKva7D9wVXPBM') 

def cat_random_gif():
	res = requests.get('https://tenor.com/search/cat-gifs')
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)
	gifElem = soup.select('img[src]')
	gif_list = []
	for i in gifElem:
		gifUrl = i.get('src')
		gif_list.append(gifUrl)
	gif_random = random.choice(gif_list)
	return gif_random

@bot.message_handler(commands=['start'])
def start_messenge(message):
	'''Принемат команду и отвечает на нее'''
	bot.send_message(message.chat.id,'Привет ! Ты нажал /start.')
	
list_answer = ['привет','hi','你好']
	
@bot.message_handler(content_types=['text'])
def send_text(message):
	'''iiohnhbkiukxokerfhfeiuwefuwehfiuwehfciuweifhkldchsjvuuweffddiogir9yuthijrijrtigjhkvojhrujhjh '''
	if 'привет' in message.text.lower():
		bot.send_message(message.chat.id, random.choice(list_answer))
		
	elif 'как дела' in message.text.lower():
		bot.send_message(message.chat.id, 'Нормально')
		
	elif 'чиво' in message.text.lower():
		bot.send_message(message.chat.id, 'Ни ЧиВо')
		
	elif 'ввв' in message.text.lower():
		bot.send_message(message.chat.id, 'ббб')
		
	elif 'кот' in message.text.lower():
		gif_cat =  cat_random_gif()
		bot.send_message(message.chat.id, gif_cat)
		
		
	else:
		bot.send_message(message.chat.id, 'мойо тебя не понимать')
		bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIETF8YKCAWUgtLCtzx0nRu18vyCrk6AAIIAAPANk8Tb2wmC94am2kaBA')
		
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
	print(message.sticker.file_id)

print('Run...')
bot.polling()


