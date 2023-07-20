# Notes
# 1. Instance Method : a. Accessors Method b. Mutator Method (use: of self)
# 2. Class Method (use: cls)
# 3. Static Method


class Student:

    #class variable
    school = "Nasiruddin"
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    #instacnce method(because we are using self)
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    #get method(getter -> only get the value)
    def get_m1(self):
        return self.m1
    
    #set method(setters(properly called mutators) -> set change the value)
    def set_m1(self, value):
        self.m1 = value

    #working with class use "cls"
    #use of decorators
    @classmethod
    def getSchool(cls):
        return cls.school


    #static method
    @staticmethod
    def info():
        print("This is a printed using static method")


    

s1 = Student(34, 55, 96)
s2 = Student(100, 100, 100)

print(s1.avg())
print(s2.avg())


