class Shakl:
    def yuza(self):
        pass


class Tortburchak(Shakl):

    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi

    def yuza(self):
        return f"To‘rtburchak yuzi: {self.eni * self.boyi}"
    

class Aylana(Shakl):

    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return f"Aylana yuzi: {3.14 * self.radius * self.radius}"
    

class Uchburchak(Shakl):

    def __init__(self, asos, balandlik):
        self.asos = asos
        self.balandlik = balandlik

    def yuza(self):
        return f"Uchburchak yuzi: {0.5 * self.asos * self.balandlik}"


tortburchak = Tortburchak(88,25)
aylana = Aylana(7)
uchburchak = Uchburchak(6, 8)

print(tortburchak.yuza())
print(aylana.yuza())
print(uchburchak.yuza())
