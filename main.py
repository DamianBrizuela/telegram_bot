from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters

from dotenv import load_dotenv
import os

load_dotenv()

Token = os.getenv("TOKEN_TELEGRAM")

def trace(message):
    print(f'::: [CHATBOT] {message}')

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Como te encuentas Usuario?')

async def bye(update: Update, context: CallbackContext):
    await update.message.reply_text('Adios, que estes bien!!')

async def chat(update: Update, context: CallbackContext):
    print(update.message.text)
    await update.message.reply_text("Chacharas")

def main():
    
    trace('RUNNING!')
    app = Application.builder().token(Token).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('bye', bye))
    app.add_handler(MessageHandler(filters.TEXT, chat))
    app.run_polling()

if __name__ == '__main__':
    main()