from flask import Flask, request, render_template
import math

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', )


@app.route('/diskriminant', methods=['GET', 'POST'])
def diskriminant():
    if request.method == 'GET':
        return render_template('diskriminant.html', )
    elif request.method == 'POST':
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))

        discr = b ** 2 - 4 * a * c

        responce = dict()
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            responce['responce'] = "D = %.2f <br> x1 = %.2f <br> x2 = %.2f" % (discr, x1, x2)
        elif discr == 0:
            x = -b / (2 * a)
            responce['responce'] = "D = %.2f <br> x = %.2f" % (discr, x)
        else:
            responce['responce'] = "Корней нет"
        return responce


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'GET':
        return render_template('guess.html', )
    elif request.method == 'POST':
        number = int(float(request.form.get('number')))
        responce = dict()
        if number > 0 and number < 60:
            responce['responce'] = 'Синий предмет'
        if number > 60 and number < 90:
            responce['responce'] = 'Зеленый предмет'
        if number > 90 and number < 100:
            responce['responce'] = 'Красный предмет'
        return responce


if __name__ == '__main__':
    app.run()
