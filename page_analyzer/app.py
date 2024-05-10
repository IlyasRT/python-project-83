from flask import Flask, render_template
from dotenv import load_dotenv
import os
import psycopg2


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')
print('app=',app)
print('app.config=',app.config)
print('app.config[\'SECRET_KEY\']=', app.config['SECRET_KEY'])
print('app.config[\'DATABASE_URL\']=', app.config['DATABASE_URL'])


@app.route('/')
def hello_world():
    # return 'Проверка --> Welcome to Flask!'
    # return render_template('index.html')
    return render_template('index2.html')
    
