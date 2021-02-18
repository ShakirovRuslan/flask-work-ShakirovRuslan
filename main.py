from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    text = """Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!"""
    page_text = '\n'.join([f"<p>{line}" for line in text.split("\n")])
    return page_text


@app.route('/image_mars')
def image_mars():
    return """
<!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src='static/img/mars.png'>
            <p>Вот она какая, Красная планета.</p>
        </body>
    </html>
"""


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
