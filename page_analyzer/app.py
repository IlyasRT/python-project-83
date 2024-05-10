from flask import Flask, render_template
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')
# print('app.config[\'DATABASE_URL\']=', app.config['DATABASE_URL'])
# conn = psycopg2.connect(DATABASE_URL)

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(app.config['DATABASE_URL'])
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
