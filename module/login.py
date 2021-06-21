from lib.database import db_connect

from flask import jsonify


def check_data_is_exist(email, password):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM public.user WHERE public.user.email = '{email}'")
    data = cur.fetchone()
    cur.close()
    conn.close()
    if email == data[0] or password == data[1]:
        return True
    return False


def login_data(email, password):
    if check_data_is_exist(email, password):
        return jsonify(
            {
                'messages': 'login complete..',
                'location': '/home',
                'error': ''
            }
        ), 200
    return jsonify(
        {
            'messages': 'failed to login, please check your email or password',
            'location': '/login',
            'error': ''
        }
    ), 401