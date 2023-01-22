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
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, milePref, typePref, powPref, peoplePref, transPref, rangePref):
        self._milePref = 'milePref'   # variables with self prefix become part of the object, 
        self._typePref = 'typePref'
        self._powPref = 'powPref'
        self._peoplePref = 'peoplePref'
        self._transPref = 'transPref'
        self._rangePref = 'rangePref'