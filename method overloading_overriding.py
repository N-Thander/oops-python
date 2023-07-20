"""
Method overloading and method overriding

note: method overloading exist in oops language like java and c++ but not in python


"""
"""
# Method Overloading

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a = None, b = None, c = None):
        
        s = 0
        
        if a != None and b != None and c != None:
           s = a + b + c
        elif a != None and b!= None:
            s = a + b
        else:
            s = a

        return s


s1 = Student(47, 88)

print(s1.sum(10, 20, 30))
"""

"""
# Method Overriding

class A:

    def show(self):
        print("in A show")

class B(A):

    def show(self):
        print("in B show")


a1 = B()
a1.show()


# because class B has its own 'show' function it overrides the 'show' function of class A despite inherting it form A this is called method overriding

"""