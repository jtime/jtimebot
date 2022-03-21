import re
import os
import urllib
import random
from linebot.models import *
from app import line_bot_api, handler
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from app import handler
from app.custom_models import PhoebeTalks

# def pretty_echo(text):
#
#     pretty_note = 'xxxxx'
#     pretty_text = ''
#
#     for i in event.message.text:
#         pretty_text += i
#         pretty_text += f"{random.choice(pretty_note)}"
#
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=pretty_text)
#     )
#
#     return True


# handle text message
@handler.add(MessageEvent, message=TextMessage)
def reply_text(event):
    if event.source.user_id != "UDSAFDSAFKJDLKSAJFDKLSJ;AFKDLS;JAF;":
        reply = False

        if not reply:
            reply = PhoebeTalks.pretty_echo(event)

        # if not reply:
        #     reply = goo_message(event)

        if not reply:
            reply = PhoebeTalks.insert_record(event)





# def goo_message(event): #goo_photo
#     msg = event.message.text
#
#     try:
#         img_search = {'tbm': 'isch', 'q': msg}
#         query = urllib.parse.urlencode(img_search)
#         base = "https://www.google.com/search?"
#         url = str(base + query)
#
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
#
#         res = urllib.request.Request(url, headers=headers)
#         con = urllib.request.urlopen(res)
#         data = con.read()
#
#         pattern = '"(https://encrypted-tbn0.gstatic.com[\S]*)"'
#         img_list = []
#
#         for match in re.finditer(pattern, str(data, "utf-8")):
#             if len(match.group(1)) < 150:
#                 img_list.append(match.group(1))
#
#         random_img_url = img_list[random.randint(0, len(img_list) + 1)]
#
#         message = ImageSendMessage(
#             original_content_url=random_img_url,
#             preview_image_url=random_img_url
#         )
#         line_bot_api.reply_message(event.reply_token, message)
#         return True
#
#     except:
#         pretty_text = PhoebeTalks.pretty_echo(event.message.text)
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text=pretty_text)
#         )
#         return False

