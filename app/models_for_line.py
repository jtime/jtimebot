from app import line_bot_api, handler

from linebot.models import MessageEvent, TextMessage, TextSendMessage
import random

@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    if event.source.user_id != "UDEADBEEFDEADBEEFDEADBEEFDEADBEEF":

        pretty_note = 'xxxxx'
        pretty_text = ''

        for i in eent.message.text:

            pretty_text += i
            pretty_text += random.choice(pretty_note)

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=pretty_text)
        )
