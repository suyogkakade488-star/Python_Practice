# using methods

class bank:
    def __init__(self):
        self.__balance = 10000
    def showbal(self):
        print("Blance: ",self.__balance)
account = bank()
account.showbal()        