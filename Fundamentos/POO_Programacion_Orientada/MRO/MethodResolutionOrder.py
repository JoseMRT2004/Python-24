class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
        super().show()

class C(A):
    def show(self):
        print("Class C")
        super().show()

class D(B, C):
    def show(self):
        print("Class D")
        super().show()

d = D()
d.show()

# """
# This example demonstrates the Method Resolution Order (MRO) in Python.
# The class D inherits from both B and C, which in turn inherit from A.
# The method resolution follows the C3 linearization (also known as the MRO algorithm).
# The expected output is:
#
# Class D
# Class B
# Class C
# Class A
#
# The order follows D → B → C → A based on Python’s MRO rules.
# """

