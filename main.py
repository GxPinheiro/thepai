import constants
import commands.phrases as phrases
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


if __name__ == '__main__':
    application = ApplicationBuilder().token(constants.API_KEY_SERVICE).build()

    application.add_handler(phrases.chegou_handler)
    application.add_handler(phrases.italiano_handler)

    application.run_polling()
