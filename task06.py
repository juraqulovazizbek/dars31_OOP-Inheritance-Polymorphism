class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        pass


class Developer(Employee):
    def calculate_bonus(self):
        return f"{self.name} ning bonus miqdori: {self.salary * 0.10}"


class Manager(Employee):
    def calculate_bonus(self):
        return f"{self.name} ning bonus miqdori: {self.salary * 0.20}"

a = Developer("Ali", 5000)
b = Manager("Vali", 8000)

print(a.calculate_bonus())
print(b.calculate_bonus())