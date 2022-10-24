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
        user.firstname = request.form['firstname']
        user.middlename = request.form['middlename']
        user.lastname = request.form['lastname']
        user.groupname = '123'
        user.username = request.form['username']
        user.password = request.form['password']
        user.mail = request.form['mail']
        user.phone = request.form['phone']
    else:
        user.firstname = request.args.get('firstname')
        user.middlename = request.args.get('middlename')
        user.lastname = request.args.get('lastname')
        user.groupname = '123'
        user.username = request.args.get('username')
        user.password = request.args.get('password')
        user.mail = request.args.get('mail')
        user.phone = request.args.get('phone')

    ORM.register_user(user)
    return render_template('register.html')


@app.route('/testorm', methods=['GET'])
def test():
    username = request.args.get('username')
    if ORM.isUserRegisteredByUsername(_username=username):
        return str(username) + " is in DB!"
    else:
        return str(username) + " is not found :("


@app.route('/getall', methods=['GET'])
def getusers():
    return ORM.getAllUsers()


if __name__ == '__main__':
    app.run(debug=True)
