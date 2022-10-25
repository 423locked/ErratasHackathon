import json, jwt
from flask import Flask, render_template, request

import os

from models.User import User

from ORM.sql_requests import ORM

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)


@app.errorhandler(Exception)
def all_exception_handler(error):
   return 'Error', 500


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


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

        if ORM.loginCheck(username,password):

            # CREATE SESSION

            if ORM.isSessionExist(username):
                pass
            
            # По-хорошему здесь надо перенапраить пользователя на другой адрес ("/dashboard")
            return render_template('dashboard.html') # Таблица из задания номер 2
        else:
            return render_template('login.html') # Отпечатать "Неправильное имя польхователя или пароль"
    else:
        return render_template('login.html')
        
'''
@app.route('/test', methods=['GET'])
def test():
    username = "loh"
    if ORM.isSessionExist(username):
        return "has"
    else:
        return "has no"  

    return str(ORM.refreshToken("mike"))
'''

if __name__ == '__main__':
    app.run(debug=True)
