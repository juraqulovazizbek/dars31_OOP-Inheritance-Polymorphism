class Animal:
    def __init__(self , name: str):
        self.name =  name        
    
    def speak(self):
        return self.name

class Dog(Animal):
    def speak(self):
        return f"{self.name} byaqa kee !"

class Cat(Animal):
    def speak(self):
        return f"{self.name} tur yuqol saripishak !"

dog = Dog("Bobik")
cat = Cat("bezbetcha")

print(dog.speak())
print(cat.speak())