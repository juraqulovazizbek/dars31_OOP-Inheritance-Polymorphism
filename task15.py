class Character:
    def __init__(self , name , tower):
        self.name = name
        self.tower = tower
    
    def attack(self):
        return f"{self.name} -> {self.tower} binosiga hujum qilmoqda."
    
    def defend(self):
        return f"{self.name} -> {self.tower} binosini himoya qilmoqda."

class Warrior(Character):
    def attack(self):
        return f"{self.name} jangchisi {self.tower} binosiga kuchli hujum qilmoqda."
    def defend(self):
        return f"{self.name} jangchisi{self.tower}ni qattiq himoya qilmoqda."



class Archer(Character):
    def attack(self):
        return f"{self.name} kamonchisi uzoqdan {self.tower}ga o‘q otmoqda."
    def defend(self):
        return f"{self.name} kamonchisi tez harakat qilib {self.tower}ni himoya qilmoqda."



class Mage(Character):
    def attack(self):
        return f"{self.name} sehrgari kuchli sehr bilan {self.tower}ni ishlatmoqda."
    def defend(self):
        return f"{self.name} sehrgari sehr bilan {self.tower}ni himoya qilmoqda."
    
a = Warrior("yeti" , "archer tower")
b = Archer("wizard" , "wizard tower")
c = Mage("valkira" , "manolit tower")

print(a.attack())
print(b.defend())
print(c.defend())
