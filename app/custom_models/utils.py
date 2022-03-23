import random
import urllib
import re
import datetime


def prepare_record(text):
    print(f"prepare_record{text}")
    text_list = text.split('\n')
    month = text_list[0].split(' ')[0].split('/')[0]
    day = text_list[0].split(' ')[0].split('/')[1]
    year = text_list[0].split(' ')[0].split('/')[2]
    d = datetime.date(int(year), int(month), int(day))
    record_list = []
    time_format = '%H:%M'
    for i in text_list[1:]:
        items = i.split(' ')
        name = items[0]
        training = items[1]
        start = datetime.datetime.strptime(items[2].split('-')[0], time_format)
        end = datetime.datetime.strptime(items[2].split('-')[1], time_format)
        duration = end - start
        record = (name, training, duration, d)
        record_list.append(record)
    print("=======================utils_prepare_record_ok====================")
    return record_list

# def goo_isch(target):
#     target = urllib.parse.quote(target)
#     url =""
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
#
#     res = urllib.request.Request(url, headers=headers)
#     con = urllib.request.urlopen(res)
#     data = con.read()
#
#     pattern = '"(https://encrypted-tbn0.gstatic.com[\S]*)"'
#     img_list = []
#
#     for match in re.finditer(pattern, str(data, "utf-8")):
#         if len(match.group(1)) < 150:
#             img_list.append(match.group(1))
#
#     random_img_url = img_list[random.randint(0, len(img_list) + 1)]
#
#     message = ImageSendMessage(
#         original_content_url=random_img_url,
#         preview_image_url=random_img_url
#     )
#     line_bot_api.reply_message(event.reply_token, message)