class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def tezligi(self):
        return f"Tezligi: {self.speed} km/h"


class Tapichka(Vehicle):
    def tezligi(self):
        return f"Onasini tapichkasidan qochayotgan  bolaning tezligi: {self.speed}🩴 km/h"


class Car(Vehicle):
    def tezligi(self):
        return f"Avtomobil tezligi: {self.speed} km/h"


tapichka = Tapichka(180)
car = Car(180)

print(tapichka.tezligi())
print(car.tezligi())
