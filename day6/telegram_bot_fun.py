from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import json
import re

ch = []
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    ch.append(chat_id)
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

#if __name__ == '__main__':
    #main()
    #print(ch)

bot_token = ''
bot_chatID = ''
bot_message = 'hello'

send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
requests.get(send_text)
