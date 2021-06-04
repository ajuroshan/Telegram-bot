from telegram import *
from telegram.ext import MessageHandler, Filters
from telegram.ext import *
import requests
# something

bot = Bot("1842457387:AAHJlh-0TR8iJAeSbLbFDhurr49WprZbUTA")

# print(bot.get_me())

updater = Updater("1842457387:AAHJlh-0TR8iJAeSbLbFDhurr49WprZbUTA",use_context=True)

dispatcher = updater.dispatcher

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def test_function(update:Update,context:CallbackContext):
	url = get_url()
	bot.send_message(chat_id = update.effective_chat.id,text = "here you go")
	bot.send_photo(chat_id =update.effective_chat.id, photo=url)


start_value = CommandHandler('start',test_function)

dispatcher.add_handler(start_value)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
