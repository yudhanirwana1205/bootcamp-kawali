#class product
class product:
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)

    def getName(self):
       return self.name

    def getprice(self):
       return self.price

    def getQuantity(self):
       return self.Quantity

    def updateQuantity(self,msl):
       self.quantity == msl

class Electronics(product):
    def __init__(self, name, price,  Quantity, warranty_period):
        super().__init__(name, price, Quantity)
        self.warranty_period = warranty_period

    def getllarrantyperiod(self):
        return self.warranty_period  


class clothing(product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size
    
    def getsize(self):
        return self.size
    
class Electonics(product):
    def __init__(self, name, price, quantity, warranty_period):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period
    

class Book(product):
    def __init__(self, name, price, quantity, outhar):
        super().__init__(name, price, quantity)
        self.author = outhar

    def getAuthor (self):
        return self.author
    



#object
fuji_film = Electonics("Fuji Film", 10000000, 50, 5)
sharp = Electonics("sharp", 5000000, 15, 3)
gucci = clothing("Gucci", 2000000, 60, "L" )
atomic_habit = Book("Book", 20000, 5, "Calck Clear")
detektif_conan_v1 = Book("detektif", 70000, 5, "detektif")