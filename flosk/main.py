from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # Домашняя страница
    return render_template('index.html')


@app.route('/contacts')
def contacts():
    # Контакты
    adress = 'Мой адресс'
    return render_template('contacts.html', adress=adress)


@app.route('/buy')
def buy():
    # Оформление заказа
    return render_template('buy.html')


@app.route('/specialoffer')
def specialoffer():
    # Cтраница с акцией
    return render_template('specialoffer.html')


if __name__ == "__main__":
    app.run()
