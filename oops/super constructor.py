class Person:
    def __init__(self, name):
        print("Person constructor")
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):
        print(self.name, self.roll_no)

s = Student("Suyog", 100)
s.display()
