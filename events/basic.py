from line_bar_api import *

def about_ius_event(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac21e6c040ab15980c9b444",
            "emojiId": "021"
        },
        {
            "index": 17,
            "productId": "5ac21e6c040ab15980c9b444",
            "emojiId": "022"
        }
    ]

    text_message = TextSendMessage(text='''
$ Master Finance $
Hello!約嗎?
'''.strip("\n"),emoji=emoji)

    sticker_message = StickerMessage(
        package_id="8522",
        sticker_id="16581271"
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message]
    )


def push_msg(event, msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id, TextSendMessage(text=msg))
    except:
        room_id = event.source.room_id
        line_bot_api.push_message(room_id, TextSendMessage(text=msg))


def Usage(event):
    push_msg(event, '''
    🌟🌟查詢方法🌟🌟   
小幫手可以查詢油價、匯率、股價

🌍油價通知 👉 輸入查詢油價
🌍匯率通知 👉 輸入查詢匯率
🌍匯率兌換 👉 輸入USD/TWD
🌍股價查詢 👉 輸入#股價代號
'''.strip("\n")
             )
