#one parent or two or more child
class animal:
    def eat(self):
        print("Eating")
class dog(animal):
    def bark(self):
         print("Barking")
class cat(animal):
    def meow(self):
        print("meowing")
        
d = dog()
c = cat()

d.eat()
d.bark()

c.eat()
c.meow()
                        