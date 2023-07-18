from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

class AddCafe(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    address = StringField("Cafe Address", validators=[DataRequired()])
    location = StringField("Cafe Location (City)", validators=[DataRequired()])
    img_url = StringField("Image URL for Cafe", validators=[DataRequired(), URL()])
    has_toilets = BooleanField("Does it have toilets?")
    has_wifi = BooleanField("Does it have wifi?")
    can_take_calls = BooleanField("Can you take calls?")
    seats = StringField("Number of seats", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price ($)", validators=[DataRequired()])
    short_description = CKEditorField("Give a short description of the Cafe", validators=[DataRequired()])
    submit = SubmitField("Add Cafe")