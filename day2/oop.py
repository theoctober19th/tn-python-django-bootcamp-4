class Car():
    def __init__(self, name):
        self.name = name

    def honk(self):
        print('I am a car named', self.name)


class Tata(Car):
    def __init__(self, name):
        self.name = name

    # def honk(self):
    #     print('I am tata named', self.name)
    

t = Tata('swift')
c = Car('swift')

t.honk()
c.honk()
