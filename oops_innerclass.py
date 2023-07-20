
# Note
# You can create object of inner class inside the outer class
# or
# You can create object of inner class outside the outer class provided you can use outer class name to call it


class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop

    def show(self):
        print(self.name, self.rollno)

    #inner class 
    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)
            


s1 = Student('Nasir', 1)
s2 = Student('Aether', 11)


