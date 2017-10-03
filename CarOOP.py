# # Assignment: Car
# # Create a class called  Car. In the__init__(), allow the user to specify the following attributes:
# price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise,
# set the tax to be 12%.
# #
# # Create six different instances of the class Car. In the class have a method called display_all()
# that returns all the information about the car as a string. In your __init__(), call this display_all()
# method to display information about the car once the attributes have been defined.
#
# A sample output would be like this:

class Car(object):
    def define_tax(self, price):
        tax = 0.00
        if price > 10001:
            tax = 0.15
        else:
            tax = 0.12
        return tax

    def __init__(self,price,speed,fuel,mileage):

        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.tax = self.define_tax(price)
        self.mileage = mileage
        self.display_all()

    def define_tax(self, price):
        tax = 0.00
        if price > 10001:
            tax = 0.15
        else:
            tax = 0.12
        return tax

    def display_all(self):

        print "Price: "+str(self.price)
        print "Speed: "+str(self.speed)+" mph"
        print "Fuel: "+ self.fuel
        print "Mileage: "+str(self.mileage)+" miles per galon"
        print "Tax: "+str(self.tax)

        return self

car1 = Car(12000,260,"full",15)
