def image_in_FlexMessage(url):
    return {"type": "image",
            "url": url,
            "size": "full",
            "aspect_ratio": "20:13",
            "aspect_mode": "cover"}

def text_in_FlexMessage(text, size, color, weight="regular", wrap=False):
    return {"type": "text",
            "text": text,
            "size": size,
            "color": color,
            "weight": weight,
            "wrap": wrap}

def logo_in_FlexMessage(text="PhoebeFlex"):
    return text_in_FlexMessage(text, size='md', color='#066BAF', weight='bold')

def title_in_FlexMessage(text):
    return text_in_FlexMessage(text, size='xl', color='#555555', weight='bold')

def heading_in_FlexMessage(text):
    return text_in_FlexMessage(text, size='xl', color='#555555')

def note_in_FlexMessage(text):
    return text_in_FlexMessage(text, size='md', color='#AAAAAA', wrap=True)

def separator_in_FlexMessage(margin= 'xl'):
    return {"type": "separator", "margin": margin}

def button_in_FlexMessage(label, data, display_text):
    return {"type": "button",
            "action": {
                "type": "postback",
                "label": label,
                "data": data,
                "display_text": display_text
            },
            "style": "link",
            "color": "#066BAF",
            "height": "sm"}

def index_Flexmessage():
    hero_image_url = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
    body_contents = [logo_in_FlexMessage(),
                     title_in_FlexMessage("Into toe alpaca_training"),
                     separator_in_FlexMessage(),
                     heading_in_FlexMessage('Overall'),
                     note_in_FlexMessage("# 查詢所有資料"),
                     heading_in_FlexMessage("alpaca_name"),
                     note_in_FlexMessage("# 按照 alpaca_name 查詢"),
                     separator_in_FlexMessage()]

    footer_contents = [button_in_FlexMessage('Overall', 'Overall', 'Overall'),
                       button_in_FlexMessage('alpaca_name', 'alpaca_name', 'alpaca_name')]

    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box',
                       'layout': 'vertical',
                       'spacing': 'md',
                       'contents': body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}
                   }
    return FlexMessage
