# parent -> child intertance of properties:


class A:
    def feature1(self):
        print('Feature 1 working')

    def feature2(self):
        print("Feature 2 working")

class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B):
    def feature5(self):
        print("Feature 5 working")



a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

c1 = C()
# C can inherte all the features form A , B and C this is called multi-level inheritance
# type in c.f -> see all the features form 1 - 5 are being inherited.

