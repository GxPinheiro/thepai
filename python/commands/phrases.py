import boto3
from telegram.ext import ContextTypes, CommandHandler

# table = boto3.resource("dynamodb", region_name='sa-east-1').Table("thepai_bot_table")
db = boto3.resource('dynamodb')
table = db.Table('thepai_bot_table')


def italiano(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="SOU ITALIANO")


def chegou(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="O Pai chegou!!")


def writetable(update, context):
    chat_id = update.message.chat_id
    response = table.put_item(
        Item={
            "id_chat ": str(chat_id),
            "lista_jogos": [
                {
                    "Nome": "Arknights",
                    "Tipo": "Gacha"
                },
                {
                    "Nome": "Blue Archive",
                    "Tipo": "Gacha"
                }
            ],
            "lista_pessoas": []
        }
    )
    context.bot.send_message(chat_id=chat_id, text="tabela")


chegou_handler = CommandHandler('chegou', chegou)
italiano_handler = CommandHandler('italiano', italiano)
write_handler = CommandHandler('table', writetable)
