import json

from flask import Flask, render_template, request

import os

from models.User import User

from ORM.sql_requests import ORM

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)


#@app.errorhandler(Exception)
#def all_exception_handler(error):
#   return 'Error', 500


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
        user.identifier = json.dumps(
            {'mail': request.form['mail'], 'phone': request.form['phone']})
        if ORM.isUserRegisteredByUsername(user.username):
            return render_template('index.html', success=False)
        else:
            ORM.register_user(user)
            return render_template('index.html', success=True)
    else:
        return render_template('index.html', )



@app.route('/testorm', methods=['GET'])
def test():
    username = request.args.get('username')
    return ORM.createToken(username)


@app.route('/getall', methods=['GET'])
def getusers():
    return ORM.getAllUsers()


if __name__ == '__main__':
    app.run(debug=True)
