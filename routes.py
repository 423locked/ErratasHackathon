from flask import Flask, render_template, request
from __main__ import app


@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Hello World!"


@app.route('/misha', methods=['GET'])
def bebra():
    return render_template('bebra.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    usernameFromPost = request.form.get('username')
    usernameFromGet = request.args.get('username')
    print('usernameFromPost = ', usernameFromPost)
    print('usernameFromGet = ', usernameFromGet)
    return "Register"


