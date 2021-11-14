from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

class AddBand(FlaskForm):
    band_name = StringField("Name: ")
    genre = StringField("Genre: ")
    founding_year = IntegerField("Year Formed: ")
    most_recent_no1 = StringField("Most Recent Number 1: ")
    no_of_members = IntegerField("Number Of Members: ")
    submit = SubmitField("Add Band")

class UpdateBand(FlaskForm):
    band_name = StringField("Name: ")
    genre = StringField("Genre: ")
    founding_year = IntegerField("Year Formed: ")
    most_recent_no1 = StringField("Most Recent Number 1: ")
    no_of_members = IntegerField("Number Of Members: ")
    submit = SubmitField("Update Band")

class AddVenue(FlaskForm):
    venue_name=StringField("Name: ")
    capacity = IntegerField("Capacity: ")
    price = IntegerField("Price: ")

class UpdateVenue(FlaskForm):
    venue_name = StringField("Name: ")
    capacity = IntegerField("Capacity: ")
    price = IntegerField("Price: ")
    

