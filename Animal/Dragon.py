from Animal import Animal

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        self.health = 170


    def fly(self):
        self.health -= 10

        return self

    def display_health(self):
        print "This is a dragon"
        super(Dragon,self).display_health()



dragon = Dragon('Carlos')

dragon.fly().display_health()
