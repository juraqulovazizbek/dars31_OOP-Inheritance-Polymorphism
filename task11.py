class Product:

    def __init__(self , name , manzil):
        self.name =name
        self.manzil = manzil
    
    def get_delivery_method(self):
        return f"{self.name } sizning buyurtmangiz {self.manzil} topshirish punktiga yetib keldi "

    def download(self):
        return f"{self.name} sizning malumotingiz {self.manzil} dan yuklab olishingiz mumkin "

class PhysicalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name } sizning buyurtmangiz {self.manzil} topshirish punktiga yetib keldi "

class DigitalProduct(Product):
        def download(self):
         return f"{self.name} sizning malumotingiz {self.manzil} dan yuklab olishingiz mumkin "

a = PhysicalProduct("ali", "loish shaharchasi Amer Temur kuchasi 3-uy ")
b = DigitalProduct("vali", "https://example.com/vali")

print(a.get_delivery_method())
print(b.download())
