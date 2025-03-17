from telegram import Update
from telegram.ext import Updater, CommandHandler

# Установите свой токен
TOKEN = '7743943724:AAH93OLyNfOoY_jT6hlf9plQ9MfX54E-zZI'

def start(update: Update, context):
    update.message.reply_text("Привет! Я бот.")

def main():
    updater = Updater(TOKEN, use_context=True)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

