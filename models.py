from application import db

class Firm(db.Model):
    name=db.Column(db.String,primary_key=True)
    year_founded=db.Integer()
    country_headquartered=db.String
    venues_owned=db.Relationship('Venues',backref='firm')
    reg_no=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    year_founded=db.Column(db.Integer(4))
    country_headquartered=db.Column(db.String)
    founder=db.Column(db.String)
    current_president=db.Column(db.String)
    db.Relationship('Venues',backref='firm')

class Venue(db.Model):
    reg_no=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    address=db.Column(db.String(50))
    capacity=db.Column(db.Integer())
    price=db.Column(db.Integer())
    dress=db.Column(db.String)
    next_performers=db.Relationship('Bands',backref='venue')
    owners=db.Column(db.String,db.ForeignKey('firm.name'))

class Band(db.Model):
    booking_no=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    genre=db.Column(db.String)
    year_formed=db.Column(db.Integer())
    most_recent_no1=db.Column(db.String)
    no_of_members=db.Column(db.Integer)
    next_concert_venue=db.Column(db.String,db.ForeignKey('venue.name'))