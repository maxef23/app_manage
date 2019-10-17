from app import app, db
from app import utils

from flask import jsonify
from flask import Response, request

import datetime
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

from app.model.UserModel import User

@app.route('/login', methods=['POST'])
def login():
    in_login = request.form['login']
    in_password = request.form['password']
    current_user = User.query.filter_by(login=in_login).first()
    if current_user is None or not current_user.password == in_password:
        return Response('Логин или пароль не верны', status=406)
    else:
        return jsonify({'token': current_user.generate_auth_token().decode('utf-8')})
