from Animal import Animal



class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        self.health = 150




Dog = Dog('Dog')

Dog.walk().run().run()
