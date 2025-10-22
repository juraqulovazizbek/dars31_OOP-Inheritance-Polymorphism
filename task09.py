class Notification:

    def __init__(self , name , xabar):
        self.name = name
        self.xabar =xabar
    
    def send(self):
        return f"{self.name}ning telifoniga {self.xabar}yuborildi"
    
class EmailNotification(Notification):
    def send(self):
        return f"{self.name}ning emailiga  {self.xabar} nomli xabaryuborildi"


class SMSNotification(Notification):
    def send(self):
        return f"{self.name}ning SMSiga  {self.xabar} nomli xabar yuborildi"
    
a = EmailNotification("Azizbek", "hello")
b = SMSNotification("Vali", 1235)

print(a.send())
print(b.send())