from flask import Flask, render_template, request

import os

from models.user import User

# from ORM.sql_requests import SQLrequest

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

    print(user)
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)