from app import line_bot_api, handler

from linebot.models import event, MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, URIAction
import random
import urllib
import re

q_string = {'tbm':'isch', 'q':event.message.text}

url = f'https://www.google.com/search?{urllib.parse.urlencode(q_string)}/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
req = urllib.request.Request(url, headers = headers)
page = urllib.request.urlopen(req)

pattern = '"(https://encrypted-tbr0.gstatic.com[\S]*)"'
img_list =[]

for match in re.finditer(pattern, str(page, 'utf-8')):
    img_list.append(match.group(0))

random_img_list = random.sample(img_list, k=5)

img_template = ImageCarouselTemplate(
    columns=[ImageCarouselColumn(image_url=url,action=URIAction(label=f'image{i}',uri=url)) for i, url in emumerate(random_img_list)]

)

line_bot_api.reply_message(
    event.reply_token,
    TemplateSendMessage(
        #alt_text=f'ImageCarousel template {}'
        template=img_template
    )
)


