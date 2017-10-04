
# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following
# requirements.
#
# Product Class:
# Attributes:
# Price
# Item Name
# Weight
# Brand
# Cost
# Status: default "for sale"

# Methods:
#
# Sell: changes status to "sold"
#
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# #
# # Return: takes reason for return as a parameter and changes status accordingly. If the item is being
# returned because it is defective change status to defective and change price to 0. If it is being returned
# in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20%
# discount.
#
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product(object):



    def __init__(self, price, itemName, weight, brand,cost):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        self.display_info()


    def display_info(self):


        print "================================================="
        print "Item: "+ self.itemName
        print "Price: " + str(self.price)
        print "Weight: " + self.weight
        print "Brand: "+ self.brand
        print "Cost: "+ str(self.cost)
        print "Status: "+ self.status
        print "================================================="

    def sell_product(self):

        self.status = "sold"
        self.display_info()
        return self

    def add_tax(self, taxDecimal):
        Tax = (self.price * taxDecimal)
        priceWTax = self.price + Tax
        print "Price with Tax: " + str(priceWTax)
        return self

    def return_item(self, reason):


        if reason == 'defective':
            self.price = 0
            self.status = 'Defective'
            self.display_info()
            return self
        elif reason == 'in the box':
            self.price = self.price
            self.status = 'for sale'
            self.display_info()
            return self
        elif reason == 'opened':
            discount = self.price * .20
            self.price = self.price - discount
            self.status = 'Used'
            self.display_info()
            return self
        else:
            print "Please enter a valid reason, you have 3 options: 'defective', 'in the box', 'opened'"
            return "Invalid Reason"
            return self


macbook = Product(2000.00,"MacBook Pro", "22 lbs", "Apple", 1200.00)

macbook.sell_product().add_tax(0.12).return_item('opened')
