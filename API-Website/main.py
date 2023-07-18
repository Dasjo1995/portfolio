from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
import requests
import random

url = 'https://hp-api.onrender.com/api/characters'

response = requests.get(url)
data = response.json()
data_list = data[:50]


app = Flask(__name__)
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf' # used for securely signing the session cookie
ckeditor = CKEditor(app)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.route('/quiz', methods=["GET", "POST"])
def characters():
    index = random.randint(0, len(data_list) - 1)
    character = data_list[index]

    return render_template('quiz.html', character=character)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)