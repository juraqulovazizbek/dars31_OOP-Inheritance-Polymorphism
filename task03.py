class User :
    def __init__(self , lvl):
       self.lvl = lvl  
    def access_level(self):
        return f"user  {self.lvl} levelda"

class Admin(User):
    def access_level(self):
     return f"Admin {self.lvl} levelda"


class Guest(User):
    def access_level(self):
        return f"Guest {self.lvl} levelda"



admin = Admin(54)
guest = Guest(45)

print(admin.access_level())
print(guest.access_level())