import json, jwt
from flask import Flask, render_template, request, url_for, redirect

import os

from models.User import User

from utils import loger

from ORM.sql_requests import ORM

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)


@app.errorhandler(Exception)
def all_exception_handler(error):
    return render_template('error.html')


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
        user.groupname = '123'
        user.username = request.form['username']
        user.password = request.form['password']
        user.identifier = json.dumps(
            {'mail': request.form['mail'], 'phone': request.form['phone']})

        if ORM.isUserRegisteredByUsername(user.username):
            return render_template('index.html', success=False)
        else:
            ORM.register_user(user)
            loger.logRegister(user.username)
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
                loger.logRefreshToken(username)
            else:
                ORM.createSession(username)
                loger.logCreateToken(username)

            # По-хорошему здесь надо перенапраить пользователя на другой адрес ("/dashboard")
            return render_template('successfulllogin.html', accessToken=ORM.getAccessToken(username)) # Таблица из задания номер 2
        else:
            return render_template('login.html', wrongCredentials=True)
    else:
        return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    token = request.args.get('accessToken')
    print(request.args.get('accessToken'))
    if request.args.get('accessToken') is not None:
        if ORM.isTokenOverdue(token):
             return redirect(url_for('login', sessionEnded=True))
        else:
            return render_template('_dashboard.html')
    else:
        print("bla")
        return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
