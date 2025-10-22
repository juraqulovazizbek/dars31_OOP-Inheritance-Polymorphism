class Dacument:

    def __init__(self , name):
        self.name = name

    def print_preview(self):
        return f"{self.name}ning dacument oynasi ochildi "

class WordDacument(Dacument):
    def print_preview(self):
        return f"{self.name}ning worddacument oynasi ochildi "

class PdfDacument(Dacument):
    def print_preview(self):
        return f"{self.name}ning pdfdacument oynasi ochildi "

a = WordDacument("ali")
b = PdfDacument("vali")

print(a.print_preview())
print(b.print_preview())
