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

    text_message = TextSendMessage(text='''$ Master Finance $
Hello!約嗎?''', emoji=emoji)

    sticker_message = StickerMessage(
        package_id="8522",
        sticker_id="16581271"
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message]
    )
