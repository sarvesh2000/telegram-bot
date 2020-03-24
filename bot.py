import telebot
BOT_API_TOKEN = '1094258301:AAFtCHuBwqp4yN5GdFYl8YFqZbSWPwTyyrg'  
bot = telebot.TeleBot(BOT_API_TOKEN)
#get updates
#updates = bot.get_updates()
#print(updates)
#Send Sample Message
#bot.send_message(chat_id="@TVS_Visitor_Entry_Bot",text="Hello")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Hello, welcome to this bot!")
bot.polling()
