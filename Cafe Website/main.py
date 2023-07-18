from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
#from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from functools import wraps
import sqlite3

from textforms import AddCafe


app = Flask(__name__)
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf' # used for securely signing the session cookie
ckeditor = CKEditor(app)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cafe(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    address = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    has_toilets = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)
    short_description = db.Column(db.String(500), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_cafes = Cafe.query.all()
    return render_template('index.html', all_cafes=all_cafes)

@app.route('/add-cafe', methods=["GET", "POST"])
def add_cafe():
    form = AddCafe()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name = form.name.data,
            address = form.address.data,
            location = form.location.data,
            img_url = form.img_url.data,
            has_toilets = form.has_toilets.data,
            has_wifi = form.has_wifi.data,
            can_take_calls = form.can_take_calls.data,
            seats = form.seats.data,
            coffee_price = form.coffee_price.data,
            short_description = form.short_description.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_cafe.html', form=form)

@app.route('/cafe-<int:cafe_id>')
def show_cafe(cafe_id):
    selected_cafe = Cafe.query.get(cafe_id)
    return render_template('show_cafe.html', selected_cafe=selected_cafe)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)