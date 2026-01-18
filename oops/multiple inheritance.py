class Father:                  # two parent class 
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass   # do nothing

c = Child()
c.skill1()
c.skill2()

print(Child.mro())              # Method Resolution Order
print(isinstance(c, Child))     # check object
print(issubclass(Child, Father))# check inheritance
