# create class [class are blueprint or templete used to create object]
class Student:
    college = "abc"   # class variable
    def __init__(self, name, marks):
        self.name = name      # instance variable
        self.marks = marks    # instance variable


# create objects [object is real instance of create from the class ]
s1 = Student('suyog', 85) #s1 are real instance(object) create from class
s2 = Student('priya', 88) #s2 are real instance(object) create from class

# access class or object(instance) variable
print(f"CLG: {s1.college}\n NAME: {s1.name}\n MARKS: {s1.marks}\n")
print(f"CLG: {s2.college}\n NAME: {s2.name}\n MARKS: {s2.marks}\n")






