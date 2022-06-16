from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def chegou(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="O Pai chegou!!")


async def italiano(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="SOU ITALIANO")


chegou_handler = CommandHandler('chegou', chegou)
italiano_handler = CommandHandler('italiano', italiano)
