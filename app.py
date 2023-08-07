# LineBot所需套件
from line_bar_api import *
from events.basic import *

app = Flask(__name__)

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

    message_text = str(event.message.text).lower()

    if message_text == "@使用說明":
        about_ius_event(event)
    if message_text == "help":
        Usage(event)


if __name__ == "__main__":
    app.run()
