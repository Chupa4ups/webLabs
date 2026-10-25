from flask import Flask
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3

app = Flask(__name__)

# Регистрация блюпринтов
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)

@app.route("/")
@app.route("/index")
def index():
    return '''<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body> 
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>
        
        <main>
            <menu>
                <li><a href="/lab1">Первая лабораторная</a></li>
                <li><a href="/lab2/">Вторая лабораторная</a></li>
                <li><a href="/lab3/">Третья лабораторная</a></li>
            </menu>
        </main>
        
        <footer>
            <hr>
            <p>Крюков Василий Александрович, ФБИ-41, 3 курс, 2026 год</p>
        </footer>
    </body>
</html>'''

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


