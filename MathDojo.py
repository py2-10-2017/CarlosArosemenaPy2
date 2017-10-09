class md(object):
    def __init__(self):
        self.total = 0

    def add(self, *num):
        for i in num:
            if type(i) is list or type(i) is tuple:
                for j in i:
                    self.total += j
            else:
                self.total += i

        return self




    def subtract(self, *num):
        for i in num:
            if type(i) is list or type(i) is tuple:
                for j in i:
                    self.total -= j
            else:
                self.total -= i

        return self


    def result(self):
        print self.total


math = md()

math.add(2).add(2,5).subtract(3,2).result()
