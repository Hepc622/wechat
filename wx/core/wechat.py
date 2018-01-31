from flask import Flask, request
from wx.config.wechat_config import *
import xml.etree.ElementTree as ET
import time
app = Flask(__name__, template_folder='pages')


@app.route("/")
def index():
    return "index"


@app.route('/wx', methods=['GET', 'POST'])
def hello_world():
    method = request.method
    if method == 'GET':
        echostr_ = request.args['echostr']
        return echostr_
    elif method == 'POST':
        # 将字符串解析成xml
        tree = ET.XML(request.data)
        to_user_name = tree.find('ToUserName').text
        from_user_name = tree.find('FromUserName').text
        content = tree.find("Content").text
        resp = text_content % (from_user_name, to_user_name, time.time(), content)
        # return resp
        return resp


if __name__ == '__main__':
    app.run(debug=True, port=80)
