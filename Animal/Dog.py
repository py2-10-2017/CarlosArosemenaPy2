from Animal import Animal



class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        self.display_health()




dog = Dog('Thor')

dog.walk().walk().walk().run().run().pet()
