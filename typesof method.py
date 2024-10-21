class Bike:
    def __init__(self):
        self.brand="Tvs"
        self.color="black"
    def start(self):
        print("tvs is strted")
    @staticmethod
    def move():
        print("tvs is moving")
    @classmethod
    def stop(cls):
        print("tvs i stopped")
b1=Bike()
print(b1.brand)
print(b1.color)
b1.start()
# b1.move()
# b1.stop()
Bike.move()
Bike.stop()