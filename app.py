from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.route("/")
@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
            <body> 
                <h1>web-сервер на flask</h1>
                <a href="/lab1/author">author</a>
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
'''

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
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

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404
