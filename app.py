from flask import Flask, render_template, request

import os

from models.User import User

from ORM.sql_requests import ORM

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    user = User()

    if request.method == 'POST':
        user.username = request.form['username']
        user.password = request.form['password']
        user.name = request.form['name']
        user.surname = request.form['surname']
    else:
        user.username = request.args.get('username')
        user.password = request.args.get('password')
        user.name = request.args.get('name')
        user.surname = request.args.get('surname')

    if ORM.isUserRegisteredByUsername(_username=user.username):
        print('USERNAME IS IN DB')
    elif ORM.isUserRegisteredByMail(_mail=user):
        print('MAIL IS IN DB')
    else:
        print("USER NOT FOUND")
    return render_template('register.html')


@app.route('/testorm', methods=['GET'])
def test():
    if ORM.isUserRegisteredByUsername(_username=user.username):
        return 'USERNAME IS IN DB'
    elif ORM.isUserRegisteredByMail(_mail=user):
        return 'MAIL IS IN DB'
    else:
        return "USER NOT FOUND"



if __name__ == '__main__':
    app.run(debug=True)
