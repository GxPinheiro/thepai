import json
import constants
import commands.phrases as phrases
from telegram.ext import Dispatcher
from telegram import Update, Bot

bot = Bot(token=constants.API_KEY_SERVICE)
dispatcher = Dispatcher(bot, None, use_context=True)


def lambda_handler(event, context):
    dispatcher.add_handler(phrases.chegou_handler)
    dispatcher.add_handler(phrases.italiano_handler)
    dispatcher.add_handler(phrases.write_handler)
    dispatcher.add_handler(phrases.get_handler)
    dispatcher.add_handler(phrases.insert_handler)


    try:
        dispatcher.process_update(
            Update.de_json(json.loads(event["body"]), bot)
        )

    except Exception as e:
        print(e)
        return {"statusCode": 500}

    return {"statusCode": 200}
