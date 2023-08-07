# LineBot所需套件
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

# Messaging API settings -> Channel access token
line_bot_api = LineBotApi("IhBapl6SZsCfsfQSEzFPgCXqE/AmmlAGpbeODS/16+GyNu53WePeBL/4NtqI1BSeLY1ZhuRp89JAjklT5VGDfvBemI/UQyIb1G4XRLGuXQ5iuyyncoXLJE3edhfF55Hm6wtK6d7XKft/l3pIwCsBNwdB04t89/1O/w1cDnyilFU=")
# Channel secret
handler = WebhookHandler("9a45400f516aa0e5128620a0181a10f9")


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Test
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)

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
    text_message = TextSendMessage(text=
'''
$ Master Finance $
Hello！您好，歡迎您成為 Master Finance 的好友
''', emoji=emoji)

    sticker_message = StickerMessage(
        package_id="8522",
        sticker_id="16581271"
    )
    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message]
    )


if __name__ == "__main__":
    app.run()
