
from app import line_bot_api
from app.custom_models import utils, CallDatabase,PhoebeFlex


from linebot.models import *
import random

def query_record(event):
    if '查詢訓練紀錄' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='query record: index', contents=PhoebeFlex.index_Flexmessage())
        )
        return True
    else:
        return False

def pretty_echo(event):

    pretty_note ="12345,09876"
    pretty_text = ""

    for i in event.message.text:

        pretty_text += i
        pretty_text += f" {random.choice(pretty_note)}"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=pretty_text)
    )
    return True

def insert_record(event):

    if '草泥馬訓練紀錄' in event.message.text:
        print("yes==========================")
        try:
            print("================in try =======================")
            record_list = utils.prepare_record(event.message.text)
            result = CallDatabase.insert(record_list)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=result)
            )


        except:
            print("insert_record except")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="失敗了")
            )
        return True
    else:
        return False