class Appliance:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass


class TV(Appliance):
    def turn_on(self):
        print("TV yoqildi. Kanal ko‘rsatilmoqda.")
    
    def turn_off(self):
        print("TV o‘chirildi.")


class Fridge(Appliance):
    def turn_on(self):
        print("Muzlatkich yoqildi. Sovutish boshlandi.")
    
    def turn_off(self):
        print("Muzlatkich o‘chirildi.")

a = TV()
b = Fridge()    

a.turn_on()

b.turn_off()