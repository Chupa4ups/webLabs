from flask import Blueprint, render_template, redirect, abort

lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return "Цветок: " + flower_list[flower_id]

@lab2.route('/lab2/flowers/')
def flowers_list():
    return f'''
    <!doctype html>
    <html>
    <body>
        <h1>Список цветов</h1>
        <p>Всего цветов: {len(flower_list)}</p>
        <ul>
            {"".join([f"<li>{flower}</li>" for flower in flower_list])}
        </ul>
        <a href="/lab2/clear_flowers">Очистить список</a>
    </body>
    </html>
    '''

@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name}</p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

@lab2.route('/lab2/add_flower/')
def add_flower_empty():
    return "вы не задали имя цветка", 400

@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return f'''
    <!doctype html>
    <html>
    <body>
        <p>Список цветов очищен!</p>
        <a href="/lab2/flowers/">К списку цветов</a>
    </body>
    </html>
    '''

@lab2.route('/lab2/example')
def example():
    name = 'Крюков Василий'
    number = 2
    course = 3
    group = 'ФБИ-41'
    fruits = [
            {'name': 'яблоки', 'price': 100},
            {'name': 'груши', 'price': 120},
            {'name': 'апельсины', 'price': 80},
            {'name': 'мандарины', 'price': 95},
            {'name': 'манго', 'price': 321}
        ]
   
    return render_template('example.html', name=name, lab_num=number, 
                           course=course, group=group, fruits=fruits)

@lab2.route('/lab2/')
def lab2_index():
    return render_template('lab2.html')

@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытиый</i> чудных..."
    return render_template('filter.html', phrase=phrase)

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('calc.html', a=a, b=b, 
                           sum=a+b, sub=a-b, mul=a*b, 
                           div=a/b if b != 0 else "ошибка (деление на 0)", 
                           pow=a**b)

@lab2.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')

@lab2.route('/lab2/calc/<int:a>')
def calc_one(a):
    return redirect(f'/lab2/calc/{a}/1')

@lab2.route('/lab2/books')
def books():
    books_list = [
        {"author": "Пушкин А.С.", "title": "Евгений Онегин", "genre": "Роман в стихах", "pages": 224},
        {"author": "Лермонтов М.Ю.", "title": "Герой нашего времени", "genre": "Роман", "pages": 240},
        {"author": "Гоголь Н.В.", "title": "Мертвые души", "genre": "Поэма", "pages": 352},
        {"author": "Толстой Л.Н.", "title": "Война и мир", "genre": "Эпопея", "pages": 1300},
        {"author": "Достоевский Ф.М.", "title": "Преступление и наказание", "genre": "Роман", "pages": 416},
        {"author": "Буглаков М.А.", "title": "Мастер и Маргарита", "genre": "Роман", "pages": 480},
        {"author": "Тургенев И.С.", "title": "Отцы и дети", "genre": "Роман", "pages": 320},
        {"author": "Гончаров И.А.", "title": "Обломов", "genre": "Роман", "pages": 384},
        {"author": "Есенин С.А.", "title": "Стихотворения", "genre": "Поэзия", "pages": 150},
        {"author": "Чехов А.П.", "title": "Рассказы", "genre": "Проза", "pages": 300}
    ]
    return render_template('books.html', books=books_list)

@lab2.route('/lab2/cars')
def american_cars():
    cars = [
        {"name": "Chevrolet Impala SS", "years": "1994–1996", "engine": "V8 5.7L", "description": "Легендарный полноразмерный седан с полицейскими корнями и мощным двигателем LT1.", "image": "impala.jpg"},
        {"name": "Dodge Viper RT/10", "years": "1992–1995", "engine": "V10 8.0L", "description": "Брутальный спорткар без электронных помощников с мотором от грузовика.", "image": "viper.jpg"},
        {"name": "Ford Mustang SVT Cobra", "years": "1993–1998", "engine": "V8 5.0L / 4.6L", "description": "Культовая заряженная версия «Мустанга» 90-х годов.", "image": "mustang90.jpg"},
        {"name": "Chevrolet Corvette Z06 (C5)", "years": "2001–2004", "engine": "V8 5.7L LS6", "description": "Настоящий убийца европейских суперкаров с потрясающей динамикой.", "image": "corvettec5.jpg"},
        {"name": "Ford GT", "years": "2004–2006", "engine": "V8 5.4L Supercharged", "description": "Возрождение легендарного гоночного автомобиля побеждавшего в Ле-Мане.", "image": "fordgt.jpg"},
        {"name": "Dodge Charger SRT8", "years": "2006–2010", "engine": "V8 6.1L HEMI", "description": "Мощный американский седан для любителей динамичной езды и классического стиля.", "image": "charger.jpg"},
        {"name": "Chevrolet Camaro SS", "years": "2010–2015", "engine": "V8 6.2L", "description": "Яркий представитель эпохи возрождения масл-каров с агрессивным дизайном.", "image": "camaro.jpg"},
        {"name": "Ford Mustang Shelby GT500", "years": "2010–2014", "engine": "V8 5.4L/5.8L Supercharged", "description": "Безумный зверь с компрессором мощностью более 600 лошадиных сил.", "image": "shelby.jpg"},
        {"name": "Cadillac CTS-V", "years": "2009–2014", "engine": "V8 6.2L Supercharged", "description": "Люксовый седан, способный соревноваться на треке с лучшими трековыми купе.", "image": "ctsv.jpg"},
        {"name": "Dodge Challenger SRT Hellcat", "years": "2015", "engine": "V8 6.2L Supercharged", "description": "Кульминация эпохи современных масл-каров с дикой мощностью в 717 л.с.", "image": "hellcat.jpg"},
        {"name": "Jeep Grand Cherokee SRT8", "years": "2012–2015", "engine": "V8 6.4L HEMI", "description": "Сверхбыстрый заряженный внедорожник для любых дорог.", "image": "jeepsrt8.jpg"},
        {"name": "Tesla Model S Performance", "years": "2012–2015", "engine": "Электромотор", "description": "Революционный американский электрокар, изменивший автомобильный мир.", "image": "models.jpg"},
        {"name": "Pontiac Firebird Trans Am", "years": "1998–2002", "engine": "V8 5.7L LS1", "description": "Последнее поколение легендарного «Понтиака» с агрессивным хищным дизайном.", "image": "firebird.jpg"},
        {"name": "GMC Syclone", "years": "1991–1992", "engine": "V6 4.3L Turbo", "description": "Ультрабыстрый пикап, который в разгоне до 100 км/ч обгонял Ferrari того времени.", "image": "syclone.jpg"},
        {"name": "Ford F-150 SVT Lightning", "years": "1999–2004", "engine": "V8 5.4L Supercharged", "description": "Заряженный спортивный пикап от подразделения SVT.", "image": "lightning.jpg"},
        {"name": "Chevrolet Corvette C6 ZR1", "years": "2009–2013", "engine": "V8 6.2L LS9", "description": "Технологический флагман компании Chevrolet с карбоновыми кузовными панелями.", "image": "zr1.jpg"},
        {"name": "Dodge Viper SRT10 (ZB I)", "years": "2003–2006", "engine": "V10 8.3L", "description": "Новое поколение бескомпромиссного американского родстера.", "image": "viper2.jpg"},
        {"name": "Chrysler 300C SRT8", "years": "2005–2010", "engine": "V8 6.1L HEMI", "description": "Автомобиль с брутальной внешностью в стиле британских лимузинов и американским мотором.", "image": "300c.jpg"},
        {"name": "Buick Regal GNX (наследие 90-х)", "years": "1987–1990", "engine": "V6 3.8L Turbo", "description": "Культовый черный турбированный седан, закрывший эпоху мощных масл-каров прошлого.", "image": "gnx.jpg"},
        {"name": "Chevrolet SSR", "years": "2003–2006", "engine": "V8 5.3L / 6.0L", "description": "Эпатажный ретро-пикап с жестким складывающимся верхом кабриолета.", "image": "ssr.jpg"}
    ]
    return render_template('cars.html', cars=cars)