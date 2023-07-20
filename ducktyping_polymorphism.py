# polymorphism => in general refers to the differnt 'forms' that an object can take
# used in a. loose coupling; b. Dependency Injection; c. Interface

"""
 ways to implement polymorphism 
1. Duck Typing
2. operator Overloading
3. Method Overloading 
4. Method Overriding

"""

"""
Duck Typing: 

Duck -> 'If a bird can quack; can swim it is a duck; walks like a duck then the bird is a duck'
similary if two methods behave in a similar manner then the form 
taken by the object is called duck method


"""



class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class Myeditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


    
class Laptop:
    
    def code(self, ide):
        ide.execute()


ide1 = Pycharm()
lap1 = Laptop()
lap1.code(ide1)


ide2 = Myeditor()
lap2 = Laptop()
lap2.code(ide2)