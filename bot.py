import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from flask import Flask, request

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация Flask приложения
app = Flask(__name__)

TOKEN = ''  # Замените на свой токен

# Команда start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет, я работаю через вебхук!')

# Функция для обработки вебхука
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = Update.de_json(json_str, application.bot)
    application.process_update(update)
    return 'OK', 200

def main():
    global application
    # Инициализация приложения
    application = Application.builder().token(TOKEN).build()

    # Добавление обработчиков команд
    application.add_handler(CommandHandler("start", start))

    # Настройка вебхука с правильным URL
    application.bot.set_webhook(url='https://striking-moth-3dlainerstudiodey-cc287415.koyeb.app/' + TOKEN)

    # Запуск Flask для получения запросов
    app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()
