"""Create database models to represent tables."""
from flask_sqlalchemy import SQLAlchemy
from events_app import db
from sqlalchemy.orm import backref


# TODO: Create a model called `Guest` with the ollowing fields:
# - id: primary key
# - name: String column
# - email: String column
# - phone: String column
# - events_attending: relationship to "Event" table with a secondary table
class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False)
    events_attending = db.relationship('Event', secondary='guest_event', back_populates='guests')

class event_type(db.Enum):
    Party = 1
    Study = 2
    Networking = 3
    Meeting = 4
    Special_Occasion = 5

# TODO: Create a model called `Event` with the following fields:
# - id: primary key
# - title: String column
# - description: String column
# - date_and_time: DateTime column
# - guests: relationship to "Guest" table with a secondary table


# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500))
    date_and_time = db.Column(db.DateTime)
    guests = db.relationship('Guest', secondary='guest_event', back_populates='events_attending')

    event_type = db.Column(db.Enum('event_type'), default=event_type.Networking)

# TODO: Create a table `guest_event_table` with the following columns:
# - event_id: Integer column (foreign key)
# - guest_id: Integer column (foreign key)

guest_event_table = db.Table('guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)