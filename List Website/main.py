from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from functools import wraps
import sqlite3

from allforms import List, LoginForm, SignupForm



app = Flask(__name__)
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf' # used for securely signing the session cookie
ckeditor = CKEditor(app)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    lists = relationship('Lists', back_populates='list_user')

class Lists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_item = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    list_user = relationship('User', back_populates='lists')

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader      # this function captures user id
def load_user(user_id):             # and here we catch it
    return User.query.get(int(user_id))


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html', current_user=current_user)

@login_required
@app.route('/lists', methods=["GET", "POST"])
def make_list():
    form = List()
    list = Lists.query.all()
    if form.validate_on_submit():
        new_item = Lists(
            list_item=form.list_item.data,
            list_user=current_user
        )
        db.session.add(new_item)
        db.session.commit()
        list = Lists.query.all()
        return render_template('make_list.html', form=form, list=list, current_user=current_user)
    return render_template('make_list.html', form=form, list=list, current_user=current_user)

@app.route('/delete-<int:list_id>', methods=["GET", "POST"])
def delete(list_id):
    list_item_delete = Lists.query.get(list_id)
    db.session.delete(list_item_delete)
    db.session.commit()
    return redirect(url_for('make_list'))


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not user.password == password:
            flash("The password is incorrect, try again.")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('make_list'))
    return render_template('login.html', login_form=login_form, current_user=current_user)

@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = SignupForm()
    if register_form.validate_on_submit():
        new_user = User(
            email=register_form.email.data,
            password=register_form.password.data
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('make_list'))
    return render_template('register.html', register_form=register_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)