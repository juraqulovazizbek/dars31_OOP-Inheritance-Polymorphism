class Courier:
    def __init__(self, customer_name, km):
        self.customer_name = customer_name
        self.km = km

    def delivery_range(self):
        pass

    def calculate_fee(self):
        pass


class BikeCourier(Courier):
    def delivery_range(self):
        return "Bike 5-10 km gacha xizmat ko‘rsatadi."

    def calculate_fee(self):
        return f"{self.customer_name}, bike kuryer narxi: {self.km * 0.3 * 10000} so‘m."


class CarCourier(Courier):
    def delivery_range(self):
        return "Car 10-30 km gacha xizmat ko‘rsatadi."

    def calculate_fee(self):
        return f"{self.customer_name}, car kuryer narxi: {self.km * 0.5 * 10000} so‘m."


class DroneCourier(Courier):
    def delivery_range(self):
        return "Drone 30-50 km gacha xizmat ko‘rsatadi."

    def calculate_fee(self):
        return f"{self.customer_name}, drone kuryer narxi: {self.km * 0.7 * 10000} so‘m."


a = BikeCourier("Vali", 2)
b = CarCourier("Ali", 15)
c = DroneCourier("G'ani", 40)

print(a.calculate_fee())
print(b.calculate_fee())
print(c.calculate_fee())
