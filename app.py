import json, jwt
from flask import Flask, render_template, request, url_for, redirect

import os

from models.User import User

from ORM.sql_requests import ORM

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)


#@app.errorhandler(Exception)
#def all_exception_handler(error):
#   return 'Error', 500


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('register'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User()

        user.firstname = request.form['firstname']
        user.middlename = request.form['middlename']
        user.lastname = request.form['lastname']
        user.groupname = '123' # ПЕРЕДЕЛАТЬ!!!
        user.username = request.form['username']
        user.password = request.form['password']
        user.identifier = json.dumps(
            {'mail': request.form['mail'], 'phone': request.form['phone']})

        # Нужно прописать обязательные и необязательный поля
        print(user)
        if ORM.isUserRegisteredByUsername(user.username):
            return render_template('index.html', success=False) # Отпечатать ошибку, что пользователь уже создан
        else:
            ORM.register_user(user)
            return render_template('index.html', success=True)
    else:
        return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if ORM.loginCheck(username, password):

            # CREATE SESSION

            if ORM.isSessionExist(username):
                ORM.refreshToken(username)
            else:
                ORM.createSession(username)

            # По-хорошему здесь надо перенапраить пользователя на другой адрес ("/dashboard")
            return render_template('successfulllogin.html', accessToken=ORM.getAccessToken(username)) # Таблица из задания номер 2
        else:
            return render_template('login.html', wrongCredentials=True) # Отпечатать "Неправильное имя польхователя или пароль"
    else:
        return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        if request.args.get('accessToken') is None:
            return render_template('dashboard.html', authenticated=False)
        elif not ORM.isTokenOverdue(request.args.get('accessToken')):
            return render_template('dashboard.html', authenticated=True)
    else:
        print('POST', request.form['accessToken'])
        if request.form['accessToken'] is None:
            return render_template('dashboard.html', authenticated=False)
        else:
            if ORM.isTokenOverdue(_token=request.form['accessToken']):
                return redirect(url_for('login'), 301)
            else:
                return render_template('dashboard.html', authenticated=True)


@app.route('/test', methods=['GET'])
def test():
    return ORM.getAccessToken("mike")


@app.route('/testvue', methods=['GET'])
def testvue():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
