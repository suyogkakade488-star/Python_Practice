class vehicle:
    def start(self):
        print("Vehicle started")
class car(vehicle):
    def drive(self):
        print("Car is Driving")
c = car()
c.start()
c.drive()