from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from flask import Flask, request
import os

# Инициализируем Flask
app = Flask(__name__)

# Токен вашего бота
TOKEN = '7743943724:AAH93OLyNfOoY_jT6hlf9plQ9MfX54E-zZI'
URL = 'https://striking-moth-3dlainerstudiodey-cc287415.koyeb.app/'

# Функция обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я бот с вебхуком.")

# Устанавливаем вебхук
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = Update.de_json(json_str, bot)
    dispatcher.process_update(update)
    return 'ok', 200

def main():
    global bot, dispatcher

    # Инициализируем бота и диспатчер
    bot = Updater(TOKEN, use_context=True).bot
    dispatcher = bot.dispatcher

    # Добавляем обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Устанавливаем вебхук на ваш публичный адрес
    bot.set_webhook(url=URL + TOKEN)

    # Запускаем Flask
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

if __name__ == '__main__':
    main()
