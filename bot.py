from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = 'YOUR_BOT_TOKEN'  # Замените на свой токен

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я бот.')

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()
