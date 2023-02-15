from flask import Flask, request, redirect

import ws

app = Flask(__name__)


@app.route('/<query>', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index(query=''):
    if request.method == 'POST':
        return redirect('/' + request.form['query'])
    print(request.method)
    if request.method == 'POST':
        query = request.form['query']
        print(123)
        print(query)
    with open('design.html', 'r', encoding='utf-8') as html_stream:
        html = html_stream.read()
        weather = ws.get_weather(query)
        for replace in weather:
            html = html.replace('{{ ' + replace + ' }}', str(weather[replace]))
        return html


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True)