class BankAccount:
    def __init__(self, name , balance):
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Hisobda yetarli mablag' yo'q."
        self.balance -= amount
        return f"{self.name} ning hisobidan {amount} so'm yechildi. Qolgan balans: {self.balance} so'm."

    def get_interest(self):
        return f"{self.name} ning yillik foiz daromadi: {self.balance * 0.2}"

class SavingsAccount(BankAccount):
    def get_interest(self):
        return f"{self.name} ning yillik foiz daromadi: {self.balance * 0.5}"
    def withdraw(self, amount):
        if amount > self.balance:
            return "Hisobda yetarli mablag' yo'q."
        self.balance -= amount
        return f"{self.name} ning jamg'arma hisobidan {amount} so'm yechildi. Qolgan balans: {self.balance} so'm."
class CheckingAccount(BankAccount):
    def get_interest(self):
        return f"{self.name} ning yillik foiz daromadi: {self.balance * 0.03}"
    def withdraw(self, amount):
        if amount > self.balance:
            return f"{self.name} ning hisobida yetarli mablag' yo'q."
        self.balance -= amount
        return f"{self.name} ning tekshiruv hisobidan {amount} so'm yechildi. Qolgan balans: {self.balance} so'm."
a = SavingsAccount("Ali", 10000)
b = CheckingAccount("Vali", 20000)

print(a.withdraw(5000))
print(b.withdraw(25000))

print(a.get_interest())
print(b.get_interest())