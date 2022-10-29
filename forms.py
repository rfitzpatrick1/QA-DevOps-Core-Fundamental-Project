from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

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
    address=StringField("Address: ")
    capacity = IntegerField("Capacity: ")
    price = IntegerField("Price: ")
    dress = StringField("Dress: ")
    submit =SubmitField("Add Venue")
    

class UpdateVenue(FlaskForm):
    venue_name = StringField("Name: ")
    address = StringField("Address: ")
    capacity = IntegerField("Capacity: ")
    price = IntegerField("Price: ")
    dress = StringField("Dress: ")
    submit = SubmitField("Update Venue")

class AddFirm(FlaskForm):
    firm_name=StringField("Name: ")
    country_headquartered=StringField("Country: ")
    founding_year=IntegerField("Year Founded: ")
    founder=StringField("Founder: ")
    current_president=StringField("President: ")

class UpdateFirm(FlaskForm):
    firm_name=StringField("Name: ")
    country_headquartered=StringField("Country: ")
    founding_year=IntegerField("Year Founded: ")
    founder=StringField("Founder: ")
    current_president=StringField("President: ")
