import json
import os
import random

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
            'rangePref':''
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
    def assign_preference(self):
        self.user_data['milePref'] =  answer
        self.user_data['typePref'] =  QnA['answer']
        self.user_data['powPref'] =  QnA['solution']

    
    # TODO: Actually do this
    def compare_cars(self):

    def get_student_data(self):
        return {
            "totalScores":  self.user_data['milePref'] ,
            "totalCorrectAnswers":  self.user_data['totalCorrectAnswers'] ,
            "totalWrongAnswers":  self.user_data['totalWrongAnswers'] ,
        }




car_info_master  = CarInfo()