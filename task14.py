class User:
    def __init__(self, name , ish):
        self.name = name
        self.ish = ish

    def interact(self):
        pass


class Applicant(User):
    def interact(self):
        return f"{self.name} {self.ish} ga ariza yubormoqda."


class Employer(User):
    def interact(self):
        return f"{self.name} {self.ish} ga yangi ish e'lon qilmoqda."


a = Applicant("Vali", "dasturchi")
b = Employer("Ali", "dasturchi")

print(a.interact())
print(b.interact())
