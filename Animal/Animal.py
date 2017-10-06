class Animal(object):
    def __init__(self, name, *health):
        self.name = name
        self.health = health




    def display_health(self):
        print "{}'s health is {}".format(self.name, self.health)

    def walk(self):
        if self.health > 0:
            self.health -= 1
            self.display_health()
        else:
            self.display_health()
            print "not enough health for {} to walk".format(self.name)


        return self

    def run(self):
        if self.health > 5:
            self.health -= 5
            self.display_health()
        else:
            self.display_health()
            print "not enough health for {} to run".format(self.name)


        return self
