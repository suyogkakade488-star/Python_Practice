# getter and setter 

class bank:
    def __init__(self):
        self.__balance = 0
    def getbal(self):
        return self.__balance
    def setbal(self,amount):
        if amount>=0:
         self.__balance = amount
        else:
            print("INvalid Amount")
acc = bank()
acc.setbal(5000)
print(acc.getbal())