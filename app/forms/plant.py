from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CreateForm(FlaskForm):
    plant_name = StringField("Plant Name")
    location = StringField("Location")
    submit = SubmitField("Create")

class ProfileForm(FlaskForm):
    plant_name = StringField("Plant Name")
    location = StringField("Location")
    submit = SubmitField("Save")