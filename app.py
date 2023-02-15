from flask import Flask

import ws

app = Flask(__name__)


@app.route('/')
def index():
    with open('design.html', 'r', encoding='utf-8') as html_stream:
        html = html_stream.read()
    weather = ws.get_weather()



if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True)