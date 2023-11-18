from telebot import TeleBot

BOT_TOKEN = 'sua_api'
bot = TeleBot(BOT_TOKEN)

@bot.message.handler(commands = ['começar', 'olá', 'oi'])
def send_welcome(message):
    bot.reply_to(message, "Olá, eu sou o Bot Jaiminho, no que poderia lhe ajudar ?")

@bot.message_handler(fund = lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()