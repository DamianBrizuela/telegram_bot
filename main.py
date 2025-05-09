from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

import os
from dotenv import load_dotenv
load_dotenv()

def trace(message):
    print(f'::: [CHATBOT] {message}')

Token = os.getenv("TOKEN_TELEGRAM")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Como te encuentas wey!!')

def main():
    trace('RUNNING!')
    trace(Token)
    app = Application.builder().token(Token).build()
    app.add_handler(CommandHandler('start', start))
    app.run_polling()

if __name__ == '__main__':
    main()