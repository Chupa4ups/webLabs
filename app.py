from flask import Flask, url_for, request, redirect, abort, render_template
from datetime import datetime


app = Flask(__name__)

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

@app.route("/lab1")
@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
            <head>
                <title>Лабораторная 1</title>
            </head>

            <body> 
                <h1>web-сервер на flask</h1>

                <p>«От нерешительности теряешь больше, чем от неверного решения»</p>
                
                    <li><a href="/lab1/author">author</a></li>
                    <li><a href="/index">На главную</a></li>
                    <li><a href="/">Ссылка на корень сайта</a></li>
                
                <h2>Меню</h2>

                    <li><a href="/lab1/author">Автор</a></li>
                    <li><a href="/lab1/image">Слон (RU)</a></li>
                    <li><a href="/lab1/image/en">Elephant (EN)</a></li>
                    <li><a href="/lab1/image/de">Elefant (DE)</a></li>
                    <li><a href="/lab1/counter">Счётчик</a></li>
                    <li><a href="/lab1/clear_counter">Очистить счётчик</a></li>
                    <li><a href="/lab1/info">Информация</a></li>
                    <li><a href="/lab1/created">Статус 201 Created</a></li>
                    <li><a href="/lab1/400">Ошибка 400 Bad Request</a></li>
                    <li><a href="/lab1/401">Ошибка 401 Unauthorized</a></li>
                    <li><a href="/lab1/402">Ошибка 402 Payment Required</a></li>
                    <li><a href="/lab1/403">Ошибка 403 Forbidden</a></li>
                    <li><a href="/lab1/405">Ошибка 405 Method Not Allowed</a></li>
                    <li><a href="/lab1/418">Ошибка 418 I'm a teapot</a></li>
                    <li><a href="/lab1/error">Ошибка 500</a></li>
                
            </body>
        </html>""", 200, {
            "X-Server": "sample",
            "Content-Type": "text/html; charset=utf-8"
            }

@app.route("/lab1/author")
def author():
    name = "Крюков василий Александрович"
    group = "ФБИ-41"
    faculty = "ФБ"
    return """<!doctype html>
        <html>
            <body> 
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body> 
        </html>"""

@app.route('/lab1/image')
def image():
    path1 = url_for("static", filename="elephant.jpg")
    path2 = url_for("static", filename="lab1.css")

    icon1 = url_for("static", filename="icon1.png")
    icon2 = url_for("static", filename="icon2.png")

    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Language": "ru",             
        "Image-Category": "Animals",        
        "Author-Group": "FBI-41"           
    }

    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="{path2}" >

        <link rel="icon" type="image/png" href="{icon1}">
        <link rel="icon" type="image/png" href="{icon2}">
    </head>
    <body> 
        <h1>Слон</h1>
        <img src="''' + path1 +'''">
    </body> 
</html>
''', 200, headers

@app.route('/lab1/image/en')
def image_en():
    path1 = url_for("static", filename="elephant.jpg")
    path2 = url_for("static", filename="lab1.css")

    icon1 = url_for("static", filename="icon1.png")
    icon2 = url_for("static", filename="icon2.png")

    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Language": "en",
        "Image-Category": "Animals",
        "Author-Group": "FBI-41"
    }

    return f'''
<!doctype html>
<html lang="en">
    <head>
        <title>Elephant</title>
        <link rel="stylesheet" href="{path2}">
        <link rel="icon" type="image/png" href="{icon1}">
        <link rel="icon" type="image/png" href="{icon2}">
    </head>
    <body> 
        <h1>Elephant</h1>
        <img src="{path1}" alt="Elephant">
    </body> 
</html>
''', 200, headers

@app.route('/lab1/image/de')
def image_de():
    path1 = url_for("static", filename="elephant.jpg")
    path2 = url_for("static", filename="lab1.css")

    icon1 = url_for("static", filename="icon1.png")
    icon2 = url_for("static", filename="icon2.png")

    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "Content-Language": "de",
        "Image-Category": "Animals",
        "Author-Group": "FBI-41"
    }

    return f'''
<!doctype html>
<html lang="de">
    <head>
        <title>Elefant</title>
        <link rel="stylesheet" href="{path2}">
        <link rel="icon" type="image/png" href="{icon1}">
        <link rel="icon" type="image/png" href="{icon2}">
    </head>
    <body> 
        <h1>Elephant</h1>
        <img src="{path1}" alt="Elephant">
    </body> 
</html>
''', 200, headers

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.today()
    url = request.url
    client_ip = request.remote_addr

    return '''
<!doctype html>
<html>
    <body> 
        СКолько раз вы сюда заходили: ''' + str(count) +'''
        <a href="/lab1/clear_counter">Очистить счётчик</a>
        <hr>
        Дата и время: ''' + str(time) + ''' <br>
        Запрошенный адрес: ''' + url + ''' <br>
        Ваш IP-андрес: ''' + url + ''' <br>
    </body> 
</html>
'''

@app.route('/lab1/clear_counter')
def clear_counter():
    global count 
    count = 0
    return redirect('/lab1/counter')

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body> 
        <h1>Создано успешно</h1>
        <div><i>Что-то создано...</i></div>
    </body> 
</html>
''', 201

access_log = []

@app.errorhandler(404)
def not_found(err):
    user_ip = request.remote_addr
    access_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    requested_url = request.url

    access_log.append({
        "ip": user_ip,
        "time": access_time,
        "url": requested_url
    })

    log_items = "".join([
            f"<li><b>[" + entry['time'] + "]</b> IP: "+ entry['ip'] + " &rarr; URL: <code> " + entry['url'] + "</code></li>"
            for entry in access_log
        ])

    return '''
<!doctype html>
<html>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: red;
            color: #333;
            text-align: center;
            padding: 50px 20px;
            margin: 0;
            line-height: 1.5;
            }

        h1 {
            font-size: 40px;
            margin: 0;
            color: #FFFFFF;
            }

        div {
            font-size: 20px;
            margin: 0;
            color: #FFFFFF;
            }

        img {
            margin-top: 20px;
            }
    </style>

    <body> 
        <hr>
        <h1>404 — Страница не найдена</h1>
        <hr>
        <title>404 — Страница не найдена</title>
        <div><b>Что делать?</b></div>
        <div><i>Проверьте адрес: Убедитесь, что вы правильно написали ссылку в строке браузера.</i></div>
        <div><i>Обновите страницу: Нажмите клавишу F5 или значок обновления. Иногда это временный сбой.</i></div>
        <div><i>Перейдите на главную: Сотрите всё после доменного имени в строке поиска, чтобы зайти на главную страницу сайта.</i></div>
        <img src="/static/404.jpg" alt="404 Not Found">

        <p><b>Ваш IP-адрес:</b> ''' + user_ip + '''</p>
        <p><b>Дата и время доступа:</b>''' + access_time + '''</p>

        <p><a href="/">Вернуться на главную страницу</a></p>

        <hr>
        <h2>Журнал запросов (Лог 404):</h2>
        <ul>
            ''' + log_items +'''
        </ul>

        <p><a href="/lab1/clear_access_log" style="color: #fff; font-weight: bold;">Очистить журнал 404</a></p>

    </body> 
</html>
''', 404

@app.route('/lab1/clear_access_log')
def clear_access_log():
    global access_log
    access_log = [] 
    return redirect('/lab1/unknown') 

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