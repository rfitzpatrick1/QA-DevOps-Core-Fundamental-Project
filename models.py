from application import db

class Venue(db.Model):
    name=db.Column(db.String,primary_key=True)
    address=db.Column(db.String(50))
    capacity=db.Column(db.Integer())
    price=db.Column(db.Integer())
    dress=db.Column(db.String)
    next_performers=db.Relationship('Bands',backref='venue')

class Band(db.Model):
    name=db.Column(db.String,primary_key=True)
    genre=db.Column(db.String)
    year_formed=db.Column(db.Integer())
    most_recent_no1=db.Column(db.String)
    no_of_members=db.Column(db.Integer)
    next_concert_venue=db.Column(db.String,db.ForeignKey('venue.name'))