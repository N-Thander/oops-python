# Constructor Inheritance
# Method Relsolution order (MRO)

# sub class can access all the features of a superclass but it is not vice versa......
# if you create object of sub class it will first find __init___ of subclass if not then it will call init of super class 

"""
class A():
    
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")



class B(A):

    #super to access the methods of the super class
    #when you create object of sub class it will call init of sub class first
    # if you have call super then it will first call init of super class then call init of sub class

    def __init__(self):
        super().__init__()
        print("in B Init")

    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")

"""

class X():
    
    def __init__(self):
        print("in X Init")

    def feature1(self):
        print("Feature 1-X")

    def feature2(self):
        print("Feature 2")

class Y():
    
    def __init__(self):
        print("in Y Init")

    def feature1(self):
        print("Feature 1-Y")

    def feature3(self):
        print("Feature 3")


class Z(X, Y):
    
    # note the arguments are form left to right so if init not defined for a sub class
    # and the same can be applied for methods i.e 
    def __init__(self):
        super().__init__()
        print("in Z Init")



a1 = Z()
