from flask import Flask, render_template
from dotenv import load_dotenv
import os
import psycopg2
from urllib.parse import urlparse

load_dotenv()
app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
#app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')
#print('app.config[\'DATABASE_URL\']=', app.config['DATABASE_URL'])
DATABASE_URL = os.getenv('DATABASE_URL')
#print('DATABASE_URL=', DATABASE_URL)
# print('DATABASE_URL=', DATABASE_URL)
#db_url = urlparse(DATABASE_URL)
#print('db_url=', db_url)
# print(os.environ['KEY'])
# print(os.getenv('KEY'))
# print('app.config[\'SECRET_KEY\']=', app.config['SECRET_KEY'])
# print('app.config[\'DATABASE_URL\']=', app.config['DATABASE_URL'])
# conn = psycopg2.connect(app.config['DATABASE_URL'])


# conn = psycopg2.connect(DATABASE_URL)
# conn = psycopg2.connect('postgresql://user_page_analyzer:psw1@localhost:5432/db_page_analyzer_1')


try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(DATABASE_URL)
    print('Establish connection to database')
    print('conn=',conn)
    
except:
    # в случае сбоя подключения будет выведено сообщение  в STDOUT
    print('Can`t establish connection to database')


@app.route('/')
def hello_world():
    # return 'Проверка --> Welcome to Flask!'
    # return render_template('index.html')
    return render_template('index2.html')


#  poetry run flask --app page_analyzer:app run
#  poetry run gunicorn -w 5 -b 127.0.0.1:5000 page_analyzer:app
#  python3 -m pip install --force-reinstall dist/*.whl
