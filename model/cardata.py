import json
import os
import random


class Car:    
    def __init__(self, type, model, miles, price):
        self._type = type    # variables with self prefix become part of the object, 
        self._model = model
        self._miles = miles
        self._price = price
        self.determine_value()
    
    # gets the name of the manufacturer or the car
    @property
    def type(self):
        return self._type
    
    # a setter function, allows name to be updated after initial object creation
    @type.setter
    def type(self, type):
        self._type = type
    
    # a model getter
    @property
    def model(self):
        return self._model

    # a setter function to set the car's model
    @model.setter
    def model(self, model):
        self._model = model
    
    # a miles getter
    @property
    def miles(self):
        return self._miles
    
    # a setter function to set the car's model
    @miles.setter
    def miles(self, miles):
        self._miles = miles

     # a price getter
    @property
    def price(self):
        return self._price

    # a setter function to set the car's price 
    @price.setter
    def price(self, price):
        self._price = price
        self.determine_value() #calls function whenever price of car changes 
         
    @property
    def value(self):
        return self._value
    
    #determines car value based on price and stores it by assigning it to object
    def determine_value(self):
        if self._price > 60000:
            self._value = "Luxury Car"
        elif self._price in range(30000, 60000):
            self._value ="Middle-end Car"
        else:
            self._value ="Low-end/Second-hand Car"

    # dictionary is customized, removing password for security purposes
    @property
    def dictionary(self):
        dict = {
            "name" : self.type,
            "color" : self.model,
            "miles" : self.miles,
            "price" : self.price,
            "value" : self.value
        }
        return dict
    
    
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.dictionary)
    
    # output command to recreate the object, uses attribute directly
    def __repr__(self):
        return f'User(type={self._type}, model={self._model}, miles={self._miles}, price={self._price})'
    

if __name__ == "__main__":
    u1 = Car(type='truck', model='impala', miles='5000', price=6000)
    print("JSON ready string:\n", u1, "\n") 
    print("Raw Variables of object:\n", vars(u1), "\n") 
    print("Raw Attributes and Methods of object:\n", dir(u1), "\n")
    print("Representation to Re-Create the object:\n", repr(u1), "\n") 


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
    def __init__(self, milePref="", typePref="", powPref="", peoplePref="", transPref="", rangePref=""):
        self._milePref = 'milePref'   # variables with self prefix become part of the object, 
        self._typePref = 'typePref'
        self._powPref = 'powPref'
        self._peoplePref = 'peoplePref'
        self._transPref = 'transPref'
        self._rangePref = 'rangePref'