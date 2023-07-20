# Notes
# Types of variable in python
# 1> Instance Variable   2> Class(Static) Variables

class Car:

    # wheels -> class variables
    wheels = 4

    def __init__(self):
        # mil, com -> instance variable
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)


Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
