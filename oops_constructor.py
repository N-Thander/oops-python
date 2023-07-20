#Notes
# Every time an object is created new space is allocated this allocation is calculated by the constructor


class Computer:
    def __init__(self):
        self.name = "Nasir"
        self.age = 20

    def update(self):
        self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age = 30
c2 = Computer()

if c1.compare(c2):
    print("They are of same age")
else:
    print("They are of different age")
