from flask import Blueprint, render_template, request, make_response, redirect
from datetime import datetime
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name') or 'аноним'
    age = request.cookies.get('age') or 'неизвестен'
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, age=age,
                           name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'red')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    
    if user == '':
        errors['user'] = 'Заполните поле!'
        
    age = request.args.get('age')
    sex = request.args.get('sex')
    
    return render_template(
        'lab3/form1.html', 
        user=user, 
        age=age, 
        sex=sex, 
        errors=errors
    )


@lab3.route('/lab3/order')
def order():
     return render_template('/lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70
        
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
        
    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    price = request.args.get('price', '')
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    background = request.args.get('background')
    if color or background:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if background:
            resp.set_cookie('background', background)
        return resp
    color_cookie = request.cookies.get('color')
    background_cookie = request.cookies.get('background')
    resp = make_response(render_template(
        'lab3/settings.html', 
        color=color_cookie, 
        background=background_cookie
    ))
    return resp


@lab3.route('/lab3/clear_settings')
def clear_settings():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('background')
    return resp


SHELVES = {
    'lower': 'нижняя',
    'upper': 'верхняя',
    'side-upper': 'верхняя боковая',
    'side-lower': 'нижняя боковая',
}


@lab3.route('/lab3/ticket')
def ticket():
    # форма отправлена, если в запросе есть хоть какие-то параметры
    if not request.args:
        return render_template('lab3/ticket.html', errors={}, form={},
                               shelves=SHELVES)

    errors = {}
    form = {
        'fio': request.args.get('fio', '').strip(),
        'shelf': request.args.get('shelf', ''),
        'linen': request.args.get('linen') == 'on',
        'baggage': request.args.get('baggage') == 'on',
        'age': request.args.get('age', '').strip(),
        'departure': request.args.get('departure', '').strip(),
        'destination': request.args.get('destination', '').strip(),
        'date': request.args.get('date', '').strip(),
        'insurance': request.args.get('insurance') == 'on',
    }

    # валидация: все поля должны быть заполнены
    for field in ('fio', 'age', 'departure', 'destination', 'date'):
        if form[field] == '':
            errors[field] = 'Заполните поле!'

    if form['shelf'] not in SHELVES:
        errors['shelf'] = 'Выберите полку!'

    # возраст: целое число от 1 до 120
    age = None
    if 'age' not in errors:
        try:
            age = int(form['age'])
        except ValueError:
            errors['age'] = 'Возраст должен быть целым числом!'
        else:
            if not 1 <= age <= 120:
                errors['age'] = 'Возраст должен быть от 1 до 120 лет!'

    # дата приходит от <input type="date"> в формате ГГГГ-ММ-ДД
    date = None
    if 'date' not in errors:
        try:
            date = datetime.strptime(form['date'], '%Y-%m-%d')
        except ValueError:
            errors['date'] = 'Некорректная дата!'

    if errors:
        return render_template('lab3/ticket.html', errors=errors, form=form,
                               shelves=SHELVES)

    # расчёт стоимости
    is_child = age < 18
    price = 700 if is_child else 1000
    extras = []
    if form['shelf'] in ('lower', 'side-lower'):
        price += 100
        extras.append(('Нижняя полка', 100))
    if form['linen']:
        price += 75
        extras.append(('Бельё', 75))
    if form['baggage']:
        price += 250
        extras.append(('Багаж', 250))
    if form['insurance']:
        price += 150
        extras.append(('Страховка', 150))

    return render_template(
        'lab3/ticket_result.html',
        form=form,
        shelf_name=SHELVES[form['shelf']],
        date=date.strftime('%d.%m.%Y'),
        is_child=is_child,
        base_price=700 if is_child else 1000,
        extras=extras,
        price=price,
    )
