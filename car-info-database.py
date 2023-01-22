import json
import os
import random
db = SQLAlchemy(app) 

# I'm still setting up and changing things, there is a TODO below, most important is assigning and comparing

# Setup for information on users that we'll keep
class CarInfo:
    car_data = []
    user_data = {
            'milePref': '', 
            'typePref': '', 
            'powPref': '',
            'peoplePref': '', 
            'transPref': '',
            'rangePref':'',
    }
    # Initialize questions
    def init(self):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, "", "car-info.json")
        self.car_info = json.load(open(json_url))
        return self.car_info


 
    # Here is something to get car names, I really don't know
    # I'm reabsorbing info right now, messing around, this probably isn't important
    def get_name(self, name):
        return self.car_info[name]

    # TODO: make this work ,Here is where I'm trying to get the info of users assigned
    def User(db.Model):
    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column(db.String(255), unique=False, nullable=False)
    _dob = db.Column(db.Date)

    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    posts = db.relationship("Post", cascade='all, delete', backref='users', lazy=True)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, uid, password="123qwerty", dob=date.today()):
        self._milePref = 'milePref'   # variables with self prefix become part of the object, 
        self._typePref = 'typePref'
        self._powPref = 'powPref'
        self._peoplePref = 'peoplePref'
        self._transPref = 'transPref'
        self._rangePref = 'rangePref'