class parent:
    def __init__(self):
        self._money = 5000   # protected variable

class child(parent):
    def show(self):
        print(self._money)

c = child()
c.show()
