from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

line_bot_api = LineBotApi('VyCyOd5UUpTvQ8FnCYp2873kKy6P4TyCE8oevushDDQXLjt0vlQvCMO7yqdj6lsp343jWnBFPNTy70oPigq6rAFLjvkzq/DFxOxLTrnK4Dk0vfnYLN2QnvgjPB9WSULHqCJ3ejZwa8tl8OZgwHz70AdB04t89/1O/w1cDnyilFU=')
hander = WebhookHandler('5647ae7e90680b17da6593ad956b03a7')

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

if __mane__ == "__main__":
    app.run()

