from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

line_bot_api = LineBotApi('5FaHipawDX9dzd0RSLxKePhVdq2b/elArpHFe77sXdCPe0kFTqHhhEhq8Ub3fWX7cEp3HNvdIt1712XB27FvdxYX4cfGyp0TDvdwxr03QYzsPXP4FKky7hXanLDlJSPIkysc2YcT1X+Z5/NYVFIHVgdB04t89/1O/w1cDnyilFU=')
hander = WebhookHandler('09e5af5af7cf554e855361c1dd8640d7')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message = TextMessage)
def echo(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

if __mane__ == "__main__":
    app.run()

