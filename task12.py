class User:

    def __init__(self , name ,kurslar ):
        self.name = name
        self.kurslar = kurslar

    def get_dashboard(self):
        return f"{self.name} uchun Dashboard:  kurslarim: {self.kurslar}"


class Student(User):
    def get_dashboard(self):
        return f"{self.name} uchun Dashboard:  kurslarim:  {self.kurslar}"


class Instructor(User):
    def get_dashboard(self):
        return f"{self.name} uchun Dashboard: Talabalar statistikasi va kurs natijalari: {self.kurslar}"


users = [
    Student("Ali", ["Python", "Matematika"]),
    Instructor("Vali", ["Python", "Dasturlash asoslari"])
]

for user in users:
    print(user.get_dashboard())
