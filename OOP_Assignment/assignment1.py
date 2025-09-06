# Assignment + Activity Combined 🚀

# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Inherited Class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)   # Call parent constructor
        self.os = os

    def call(self, number):
        return f"Calling {number} using {self.brand} {self.model} 📞"

    def info(self):
        return f"{self.brand} {self.model} running {self.os}"

# Inherited Class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read(self):
        return f"Reading '{self.title}' by {self.author} 📖"

# Activity 2: Polymorphism Example
class Vehicle:
    def move(self):
        return "Vehicle is moving 🚙"

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# -------------------------------
# Create objects and test them
# -------------------------------

# Smartphone objects
phone1 = Smartphone("Apple", "iPhone 14", "iOS")
phone2 = Smartphone("Samsung", "Galaxy S23", "Android")

print(phone1.call("0712345678"))
print(phone2.info())

# Book object
book1 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")
print(book1.read())

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
