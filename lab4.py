from flask import Blueprint, render_template, redirect, request
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
    {'login': 'alex', 'password': '123'},
    {'login': 'bob', 'password': '555'},
    {'login': 'anna', 'password': '777'},
    {'login': 'max', 'password': '999'},
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab4/login.html', authorized=False)

    login = request.form.get('login')
    password = request.form.get('password')

    for user in users:
        if login == user['login'] and password == user['password']:
            return render_template('lab4/login.html', login=login, authorized=True)

    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False)