# LineBot所需套件
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

# Messaging API settings -> Channel access token
line_bot_api = LineBotApi("IhBapl6SZsCfsfQSEzFPgCXqE/AmmlAGpbeODS/16+GyNu53WePeBL/4NtqI1BSeLY1ZhuRp89JAjklT5VGDfvBemI/UQyIb1G4XRLGuXQ5iuyyncoXLJE3edhfF55Hm6wtK6d7XKft/l3pIwCsBNwdB04t89/1O/w1cDnyilFU=")
# Channel secret
handler = WebhookHandler("9a45400f516aa0e5128620a0181a10f9")
