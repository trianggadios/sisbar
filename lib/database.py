import psycopg2
import os

def db_connect():
    host = os.environ.get('DB_HOST')
    database = os.environ.get('DB_DATABASE')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    return conn