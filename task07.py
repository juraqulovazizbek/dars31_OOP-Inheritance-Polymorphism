class Media:

    def __init__(self , name):
        self.name = name
    
    def play(self):
        return f"{self.name} media ijro etilmoqda."
    
class song(Media):

    def play(self):
        return f"{self.name} qo'shig'i ijro etilmoqda." 
    
class Movie(Media):
    def play(self):
        return f"{self.name} filmi ijro etilmoqda."

class Podcast(Media):
    def play(self):
        return f"{self.name} podkast ijro etilmoqda."
    
a = song("jaloliddin Ahmadalayev")
b = Movie("formula 1")
c = Podcast("The Daily")

print(a.play())
print(b.play()) 
print(c.play())