# Optional Assignment: Store
# Now, let's build a store to contain our products by making a store class and putting our products into an array.
#
# Store class:
# Attributes:
#
#  products: an array of products objects
#
#  location: store address
#
#  owner: store owner's name
# Methods:
#
#  add_product: add a product to the store's product list
#
#  remove_product: should remove a product according to the product name
#
#  inventory: print relevant information about each product in the store
# You should be able to test your classes by instantiating new objects of each class and
# using the outlined methods to demonstrate that they work.

from Product import Product


class Store(object):


    def __init__(self,address,ownername):
        self.address = address
        self.ownername = ownername
        self.products = []
        self.inventory()


    def add_product(self, price, itemName, weight, brand,cost):

        product = Product(price,itemName,weight,brand,cost)
        self.products.append(product)
        self.inventory()

        return self

    def remove_product(self, productname):
        if self.products:
            for product in self.products:
                if productname == product.itemName:
                    self.products.pop(self.products.index(product))
                    self.inventory()



    def inventory(self):
        print "Product Name   ||   Price   ||   Weight   ||   Brand  ||   Cost"
        print "================================================================"

        if self.products:
            for product in self.products:
                    print product.itemName+"   ||   "+str(product.price)+"   ||   "+product.weight+"   ||   "+product.brand+"   ||   "+str(product.cost)
        else:
            print "no products to display"


Walmart = Store("Canada", "Carlos")

Walmart.add_product(200.00,"Carlosproduct","10 kg", "carlosbrand", 100.00).add_product(300.00,"sampleprod2","20kg","apple",150.00)

Walmart.remove_product('sampleprod2')
