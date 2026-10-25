from flask import Flask, url_for, request, redirect, abort, render_template
from datetime import datetime
from lab1 import lab1 

app = Flask(__name__)
app.register_blueprint(lab1)

@app.route("/")
@app.route("/index")
def index():
    return """<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body> 
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>
        
        <main>
            <menu>3
                <li><a href="/lab1">Первая лабораторная</a></li>
                <li><a href="/lab2/">Вторая лабораторная</a></li>
            </menu>
        </main>
        
        <footer>
            <hr>
            <p>Крюков Василий Александрович, ФБИ-41, 3 курс, 2026 год</p>
        </footer>
    </body>
</html>"""



@app.route("/lab1/400")
def code400():
    return """<!doctype html>
<html>
    <head><title>400 Bad Request</title></head>
    <body>
        <h1>400 Bad Request — Плохой запрос</h1>
        <p>Сервер не смог понять запрос из-за недействительного синтаксиса.</p>
    </body>
</html>""", 400

@app.route("/lab1/401")
def code401():
    return """<!doctype html>
<html>
    <head><title>401 Unauthorized</title></head>
    <body>
        <h1>401 Unauthorized — Не авторизован</h1>
        <p>Для доступа к запрашиваемому ресурсу требуется аутентификация.</p>
    </body>
</html>""", 401

@app.route("/lab1/402")
def code_402():
    return """<!doctype html>
<html>
    <head><title>402 Payment Required</title></head>
    <body>
        <h1>402 Payment Required — Необходима оплата</h1>
        <p>Этот код зарезервирован для будущего использования. Доступ к ресурсу требует оплаты.</p>
    </body>
</html>""", 402


@app.route("/lab1/403")
def code_403():
    return """<!doctype html>
<html>
    <head><title>403 Forbidden</title></head>
    <body>
        <h1>403 Forbidden — Запрещено</h1>
        <p>У вас нет прав для просмотра этого ресурса.</p>
    </body>
</html>""", 403


@app.route("/lab1/405")
def code_405():
    return """<!doctype html>
<html>
    <head><title>405 Method Not Allowed</title></head>
    <body>
        <h1>405 Method Not Allowed — Метод не поддерживается</h1>
        <p>Метод запроса не поддерживается для указанного ресурса.</p>
    </body>
</html>""", 405


@app.route("/lab1/418")
def code_418():
    return """<!doctype html>
<html>
    <head><title>418 I'm a teapot</title></head>
    <body>
        <h1>418 I'm a teapot — Я чайник</h1>
        <p>Сервер отказывается заваривать кофе, потому что он чайник.</p>
    </body>
</html>""", 418

@app.route("/lab1/error")
def trigger_error():
    return 1 / 0 

@app.errorhandler(500)
def internal_server_error(err):
    return """<!doctype html>
<html>
    <head><title>500 - Внутренняя ошибка сервера</title></head>
    <body>
        <h1>500 - Внутренняя ошибка сервера</h1>
        <p>Сервер столкнулся с неожиданной проблемой и не смог выполнить запрос.</p>
    </body>
</html>""", 500, {
    "Content-Type": "text/html; charset=utf-8",
    "Content-Language": "ru"
    }


"=============================================lab_2==============================================="

@app.route('/lab2/a')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        return "Цветок: " + flower_list[flower_id]

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/')
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

@app.route('/lab2/add_flower/<name>')
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
@app.route('/lab2/add_flower/')
def add_flower_empty():
    return "вы не задали имя цветка", 400

@app.route('/lab2/clear_flowers')
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

@app.route('/lab2/example')
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

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытиый</i> чудных..."
    return render_template('filter.html', phrase=phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('calc.html', a=a, b=b, 
                           sum=a+b, sub=a-b, mul=a*b, 
                           div=a/b if b != 0 else "ошибка (деление на 0)", 
                           pow=a**b)

@app.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')

@app.route('/lab2/calc/<int:a>')
def calc_one(a):
    return redirect(f'/lab2/calc/{a}/1')

@app.route('/lab2/books')
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

@app.route('/lab2/cars')
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