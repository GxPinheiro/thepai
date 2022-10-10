import boto3
from telegram.ext import ContextTypes, CommandHandler

# table = boto3.resource("dynamodb", region_name='sa-east-1').Table("thepai_bot_table")
db = boto3.resource('dynamodb', 'sa-east-1')
table = db.Table('thepai_bot_table')


def italiano(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="SOU ITALIANO")


def chegou(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="O Pai chegou!!!")


def top(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="The Pai is very top!!!")


def teste(update, context):
    chat_id = update.message.chat_id
    message = update.message.text
    context.bot.send_message(chat_id=chat_id, text="O pai é um papagaio: "+message)


def getmessage(update, context):
    chat_id = update.message.chat_id
    print(chat_id)
    response = table.get_item(Key={'id_chat': str(chat_id)})
    print(response)
    context.bot.send_message(chat_id=chat_id, text="Jogo "+response.lista_jogos.get[0])


def writetable(update, context):
    chat_id = update.message.chat_id
    response = table.put_item(
        Item={
            "id_chat": str(chat_id),
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
top_handler = CommandHandler('top', top)
write_handler = CommandHandler('table', writetable)
get_handler = CommandHandler('teste1', teste)
insert_handler = CommandHandler('teste2', getmessage)
