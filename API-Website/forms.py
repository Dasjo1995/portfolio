from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

class Quiz(FlaskForm):
    house = StringField("What is the character's house?", validators=[DataRequired()])
    ancestry = StringField("What is the character's ancestry?", validators=[DataRequired()])
    wand_core = StringField("What is their wand core?", validators=[DataRequired()])
    patronus = StringField("What is their patronus shape?", validators=[DataRequired()])
    submit = SubmitField("See if you were correct")
