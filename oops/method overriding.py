class Parent:
    def show(self):
        print("This is parent")

class Child(Parent):
    def show(self):
        super().show()
        print("This is child")

c = Child()   # object creation
c.show()
