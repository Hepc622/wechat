from flask import Flask, request, redirect
import _elementtree as el
app = Flask(__name__, template_folder='pages')


@app.route('/wx', methods=['GET', 'POST'])
def hello_world():
    method = request.method
    if method == 'GET':
        echostr_ = request.args['echostr']
        return echostr_
    elif method == 'POST':
        print(request.data)
        xml_recv = el.XMLParser
        to_user_name = xml_recv.find("ToUserName").text
        from_user_name = xml_recv.find("FromUserName").text
        content = xml_recv.find("Content").text
        print(content)
        return content


if __name__ == '__main__':
    app.run(debug=True, port=80)
