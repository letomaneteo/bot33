import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Вставь сюда свой токен
TOKEN = 'YOUR_BOT_TOKEN'

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    user_name = update.message.from_user.first_name
    update.message.reply_text(f'Привет, {user_name}! Я твой простой бот.')

# Основная функция для запуска бота
def main() -> None:
    # Создаем Updater и передаем токен
    updater = Updater(TOKEN)

    # Получаем диспетчер для обработки команд
    dp = updater.dispatcher

    # Добавляем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()

if __name__ == '__main__':
    main()
