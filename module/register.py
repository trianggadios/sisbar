from lib.database import db_connect

from flask import jsonify


def check_data_is_exist(email):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM public.user WHERE public.user.email = '{email}'")
    data = cur.fetchone()
    cur.close()
    conn.close()
    if data:
        return data
    return None


def insert_new_user_data(email, password, name):
    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO public.user VALUES ('{email}', '{password}', '{name}')")
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(
            {
                'messages': 'success create account, please login...',
                'location': '/login',
                'error': ''
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                'messages': 'failed create account',
                'location': '/login',
                'error': f'{e}'
            }
        ), 201


def register_data(email, password, name):
    if check_data_is_exist(email):
        return jsonify(
            {
                'messages': 'account already registered, please login...',
                'location': '/login',
                'error': ''
            }
        ), 301
    return insert_new_user_data(email, password, name)
