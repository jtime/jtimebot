import random
import urllib
import re
import datetime as dd


def prepare_record(text):
    #print(f"prepare_record{text}")
    text_list = text.split('\n')
    print(text_list)
    month = text_list[0].split(' ')[0].split('/')[0]
    day = text_list[0].split(' ')[0].split('/')[1]
    year = text_list[0].split(' ')[0].split('/')[2]
    d = dd.date(int(year), int(month), int(day))
    record_list = []
    time_format = '%H:%M'

    for i in text_list[1:]:
        items = i.split(' ')
        print(items)
        name = items[0]
        print(name)
        training = items[1]

        aa = "09:00"
        print(type(aa))
        startaa = dd.datetime.strptime(aa, time_format)
        print(type(startaa))

        bb = "10:37"
        print(type(bb))
        startbb = dd.datetime.strptime(bb, time_format)
        print(type(startbb))

        duration = startbb - startaa
        print(duration)

        # start1 = items[2].split('-')[0]
        # print(type(start1))
        # #start = dd.strptime(items[2].split('-')[0], time_format)
        # start = dd.datetime.strptime(start1, time_format)
        # print(start)
        #
        # end = dd.datetime.strptime(items[2].split('-')[1], time_format)
        # print(end)
        # duration = end - start
        print(duration, d)
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