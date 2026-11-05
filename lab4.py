from flask import Blueprint, render_template, redirect, request, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='На нольделить нельзя!')
    result = x1 / x2
    return render_template('lab4/div-result.html', x1=x1, x2=x2, result=result)


# Суммирование
@lab4.route('/lab4/add-form')
def add_form():
    return render_template('lab4/add-form.html')

@lab4.route('/lab4/add', methods=['POST'])
def add():
    x1_str = request.form.get('x1')
    x2_str = request.form.get('x2')
    
    # Если какое-либо поле пустое, считаем, что ввели 0
    x1 = int(x1_str) if x1_str != '' else 0
    x2 = int(x2_str) if x2_str != '' else 0
    
    result = x1 + x2
    return render_template('lab4/arithmetic.html', x1=x1, x2=x2, sign='+', result=result, back_url='/lab4/add-form')


# Вычитание
@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1_str = request.form.get('x1')
    x2_str = request.form.get('x2')
    
    # Выдавать ошибку при пустых полях
    if x1_str == '' or x2_str == '':
        return render_template('lab4/arithmetic.html', error='Оба поля должны быть заполнены!', back_url='/lab4/sub-form')
    
    x1 = int(x1_str)
    x2 = int(x2_str)
    result = x1 - x2
    return render_template('lab4/arithmetic.html', x1=x1, x2=x2, sign='-', result=result, back_url='/lab4/sub-form')


# Умножение
@lab4.route('/lab4/mul-form')
def mul_form():
    return render_template('lab4/mul-form.html')

@lab4.route('/lab4/mul', methods=['POST'])
def mul():
    x1_str = request.form.get('x1')
    x2_str = request.form.get('x2')
    
    # Если какое-либо поле пустое, считать, что ввели 1
    x1 = int(x1_str) if x1_str != '' else 1
    x2 = int(x2_str) if x2_str != '' else 1
    
    result = x1 * x2
    return render_template('lab4/arithmetic.html', x1=x1, x2=x2, sign='*', result=result, back_url='/lab4/mul-form')


# Возведение в степень
@lab4.route('/lab4/pow-form')
def pow_form():
    return render_template('lab4/pow-form.html')

@lab4.route('/lab4/pow', methods=['POST'])
def pow_num():
    x1_str = request.form.get('x1')
    x2_str = request.form.get('x2')
    
    # Ошибка при пустых полях
    if x1_str == '' or x2_str == '':
        return render_template('lab4/arithmetic.html', error='Оба поля должны быть заполнены!', back_url='/lab4/pow-form')
    
    x1 = int(x1_str)
    x2 = int(x2_str)
    
    # Ошибка, если оба поля равны нулю
    if x1 == 0 and x2 == 0:
        return render_template('lab4/arithmetic.html', error='Оба поля не могут быть равны нулю одновременно!', back_url='/lab4/pow-form')
    
    result = x1 ** x2
    return render_template('lab4/arithmetic.html', x1=x1, x2=x2, sign='^', result=result, back_url='/lab4/pow-form')


tree_count = 0

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count

    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)

    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < 10:
            tree_count += 1

    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Алексей Иванов', 'gender': 'м'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Smith', 'gender': 'м'},
    {'login': 'anna', 'password': '777', 'name': 'Анна Петрова', 'gender': 'ж'},
    {'login': 'max', 'password': '999', 'name': 'Максим Сидоров', 'gender': 'м'},
]

def get_user(login):
    for user in users:
        if user['login'] == login:
            return user
    return None


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        user = get_user(session.get('login'))
        if user:
            return render_template('lab4/login.html', authorized=True, name=user['name'])
        return render_template('lab4/login.html', authorized=False, login='')

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        return render_template('lab4/login.html', authorized=False,
                               error='Не введён логин', login=login)
    if not password:
        return render_template('lab4/login.html', authorized=False,
                               error='Не введён пароль', login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')

    return render_template('lab4/login.html', authorized=False,
                           error='Неверные логин и/или пароль', login=login)


@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'GET':
        return render_template('lab4/weather.html')

    raw = request.form.get('temperature', '').strip().replace(',', '.')
    if raw == '':
        return render_template('lab4/weather.html', error='ошибка: не задана температура')
    try:
        t = float(raw)
    except ValueError:
        return render_template('lab4/weather.html', error='ошибка: температура должна быть числом')

    shown = int(t) if t == int(t) else t

    if t < -30:
        message = 'слишком холодно'
    elif t > 30:
        message = 'слишком жарко'
    elif t <= -17:
        message = f'Очень холодно. Температура: {shown}°С'
    elif t <= 0:
        message = f'Холодно. Температура: {shown}°С'
    elif t <= 15:
        message = f'Прохладно. Температура: {shown}°С'
    elif t <= 25:
        message = f'Тепло. Температура: {shown}°С'
    else:
        message = f'Жарко. Температура: {shown}°С'

    return render_template('lab4/weather.html', message=message, temperature=raw)


CONCRETE_PRICES = {'М200': 4200, 'М300': 4800, 'М400': 5400, 'М500': 6100}


@lab4.route('/lab4/concrete', methods=['GET', 'POST'])
def concrete():
    if request.method == 'GET':
        return render_template('lab4/concrete.html', prices=CONCRETE_PRICES, kind='М200')

    kind = request.form.get('kind')
    raw = request.form.get('volume', '').strip().replace(',', '.')

    def fail(text):
        return render_template('lab4/concrete.html', prices=CONCRETE_PRICES,
                               kind=kind, volume=raw, error=text)

    if kind not in CONCRETE_PRICES:
        return fail('Выберите марку бетона')
    if raw == '':
        return fail('Не указан объём')
    try:
        volume = float(raw)
    except ValueError:
        return fail('Объём должен быть числом')
    if volume <= 0:
        return fail('Объём должен быть больше нуля')
    if volume > 100:
        return fail('Такого объёма сейчас нет в наличии')

    total = volume * CONCRETE_PRICES[kind]
    discount = 0
    if volume > 10:
        discount = total * 0.10
        total -= discount

    return render_template('lab4/concrete.html', prices=CONCRETE_PRICES, kind=kind,
                           volume=raw, ordered=True, shown_volume=round(volume, 2),
                           total=round(total, 2), discount=round(discount, 2))
