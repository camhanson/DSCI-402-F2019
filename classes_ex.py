#Illustrate basic object-oriented programming via class creation.
import math 

class Vehicle:
    def __init__ (self, name, location, direction, mpg = 1.0, fuel_level=0, mileage=0):
        self.name = name
        self.location = location
        self.direction = direction 
        self.mpg = mpg
        self.fuel_level = fuel_level
        self.mileage = mileage
    def print_info(self):
        print('Vehicle Info')
        print('   Name:  '  + str(self.name))
        print('   Location:  ' + str(self.location))
        print('   Direction:  ' + str(self.direction))
        print('   Mpg:     ' + str (self.mpg))
        print('   Mileage:  '  + str(self.mileage))
        print('   Fuel Level:  ' + str(self.fuel_level) + ' Gallons')
    def go(self,distance):  
        if distance <= (self.fuel_level*self.mpg):
            s = distance/math.sqrt(self.direction[0]^2 + self.direction[1]^2)
            self.location = (round(self.location[0]+(s*self.direction[0]),2),round(self.location[1] + (s*self.direction[1]),2))
            self.fuel_level = (self.fuel_level - distance/self.mpg)
            self.mileage = (self.mileage + distance)
        else:
            print('Cannot go this distance. Not enough Fuel!') 

class Car(Vehicle):
    def __init__ (self, name, location, direction, mpg, fuel_level=0, mileage=0):
        super().__init__(name, location, direction, mpg, fuel_level, mileage)
   
       