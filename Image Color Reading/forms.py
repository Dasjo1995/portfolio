from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

class Upload(FlaskForm):
    file = FileField("")
    submit = SubmitField("Upload File")