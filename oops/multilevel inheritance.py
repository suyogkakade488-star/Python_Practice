class  grandfather:
    def house (self):
        print("house")
class father(grandfather):
    def car(self):
        print("car")
class son (father):
    def bike(self):
        print("bike")

s = son()
s.house()
s.bike()
s.car()