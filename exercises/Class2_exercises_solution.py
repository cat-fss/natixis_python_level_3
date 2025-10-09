"""
Exercise 1 & 2
- Create a class named "Animal" with "age" and "name" attributes. Age should default to 0 and be protected.
- Add a method called describe() to the Animal class that returns "This animal is called [name] and is [age] years old."
- Call describe()
- Create a method in the Animal class called celebrate_birthday that increases age by 1 and calls describe(). Call the celebrate_birthday() method.
"""

class Animal:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def describe(self):
        return f"This animal is called {self.name} and is {self.__age} years old."
    
    def celebrate_birthday(self):
        self.__age +=1
        return self.describe()
    

snake = Animal("snake", 2)
snake.describe()
snake.celebrate_birthday()

"""
Exercise 3
Create a class Person with attributes: name, age (protected), and personal_id (private) and method introduce, that returns "Hello, my name is [name] and I am [age] years old."

"""
class Person:
    def __init__(self, name, age, personal_id = "Unknown"):
        self.name = name
        self._age = age
        self.__personal_id = personal_id

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self._age} years old."
    

p1 = Person("Anna", 20)
p1.introduce()

"""
Exercise 4
Create subclasses Student and Teacher that inherit from Person. Each one should add a new attribute:
Student: student_id
Teacher: subject
"""
class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

s1 = Student("João", 20, "S123")
t1 = Teacher("Dr. Silva", 45, "Mathematics")
s1.introduce()
t1.introduce()

"""
Exercise 5
Give each subclass its own version of introduce(), showing their specific role
"""

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"I'm {self.name}, a student with ID {self.student_id}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"I'm Professor {self.name}, and I teach {self.subject}.")

s2 = Student("João", 20, "S123")
t2 = Teacher("Dr. Silva", 45, "Mathematics")
s2.introduce()
t2.introduce()

"""
Exercise 6
Write a function introduce_person(person) that calls person.introduce() for any object that has that method.
"""
def introduce_person(person):
    person.introduce()

introduce_person(Student("Carla", 21, "S456"))
introduce_person(Teacher("Dr. Rocha", 55, "Physics"))

"""
Exercise 7
- Add a private attribute __email to Person.
- Create a method show_email() to display it safely.
- Try to print email from outside the class without show_email().
"""
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self._age = age
        self.__email = email  # private attribute

    def show_email(self):
        return f"Email: {self.__email}"

p1 = Person("Rita", 30, "rita@uni.pt")
p1.show_email()
# print(p1.__email)  # would fail (AttributeError)

"""
Exercise 8
- Create a base class called Device:
    - It should have attributes: brand, _model (protected), and __price (private).
    - It should have a method display_info() that prints all these attributes.

- Create two subclasses:
    - Phone
    - Laptop

- Each subclass should:
    - Call the base constructor.
    - Override display_info() to include an identifying message before printing the attributes (e.g., "This is a phone.").

- Demonstrate creating instances of both subclasses, accessing public and protected attributes directly, and 
attempting to access the private attribute.

Expected Output:
This is a phone.
Brand: Apple
Model: iPhone 15
Price: 1299
This is a laptop.
Brand: Dell
Model: XPS 15
Price: 1999
"""
class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model       # protected
        self.__price = price      # private

    def display_info(self):
        print(f"Brand: {self.brand}\nModel: {self._model}\nPrice: {self.__price}")

class Phone(Device):
    def display_info(self):
        print("This is a phone.")
        super().display_info()

class Laptop(Device):
    def display_info(self):
        print("This is a laptop.")
        Device.display_info(self)  # same as super

# Demonstration
phone = Phone("Apple", "iPhone 15", 1299)
laptop = Laptop("Dell", "XPS 15", 1999)

# Public and protected access (works)
print(phone.brand)
print(phone._model)

# Private access (fails)
# print(phone.__price)  # AttributeError

# Use methods to display info
phone.display_info()
laptop.display_info()

"""
Exercise 9
- Modify the Device class to make it abstract using the abc module.
    - Import ABC and abstractmethod.
    - Define an abstract method called get_specs() that must be implemented by all subclasses.

- Update the Phone and Laptop classes to implement get_specs().
    - Each implementation should print device-specific details.

- Demonstrate creating instances of Phone and Laptop, and calling get_specs() on both.

Expected Output:
Phone Specifications → Brand: Apple, Model: iPhone 15, Price: 1299
Laptop Specifications → Brand: Dell, Model: XPS 15, Price: 1999
"""
from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price

    @abstractmethod
    def get_specs(self):
        pass

class Phone(Device):
    def get_specs(self):
        price = self._Device__price
        return f"Phone Specifications → Brand: {self.brand}, Model: {self._model}, Price: {price}"

class Laptop(Device):
    def get_specs(self):
        price = self._Device__price
        return f"Laptop Specifications → Brand: {self.brand}, Model: {self._model}, Price: {price}"

# Demonstration
phone = Phone("Apple", "iPhone 15", 1299)
laptop = Laptop("Dell", "XPS 15", 1999)

phone.get_specs()
laptop.get_specs()


"""
Exercise 10
- Convert Device back into a regular class (not abstract).
- Keep the get_specs() method but give it a default implementation.
- Add another subclass: Tablet.
    - Override get_specs() with a tablet-specific message.

- Create a function display_specs(device) that accepts any Device object and calls get_specs().
- Demonstrate passing instances of Phone, Laptop, and Tablet.

Expected Output:
Phone Specifications → Brand: Apple, Model: iPhone 15, Price: 1299
Laptop Specifications → Brand: Dell, Model: XPS 15, Price: 1999
Tablet Specifications → Brand: Samsung, Model: Galaxy Tab, Price: 899
"""
class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price

    def get_specs(self):
        print(f"Device → Brand: {self.brand}, Model: {self._model}, Price: {self._Device__price}")

class Phone(Device):
    def get_specs(self):
        print(f"Phone Specifications → Brand: {self.brand}, Model: {self._model}, Price: {self._Device__price}")

class Laptop(Device):
    def get_specs(self):
        print(f"Laptop Specifications → Brand: {self.brand}, Model: {self._model}, Price: {self._Device__price}")

class Tablet(Device):
    def get_specs(self):
        print(f"Tablet Specifications → Brand: {self.brand}, Model: {self._model}, Price: {self._Device__price}")

def display_specs(device):
    device.get_specs()

# Demonstration
phone = Phone("Apple", "iPhone 15", 1299)
laptop = Laptop("Dell", "XPS 15", 1999)
tablet = Tablet("Samsung", "Galaxy Tab", 899)

for d in [phone, laptop, tablet]:
    display_specs(d)


"""
Exercise 11
- Create two unrelated classes: Printer and Projector.
    - Each should have a method display() that returns an appropriate message.

- Create a function show_device_output(device) that calls the display() method.
- Demonstrate polymorphism by passing both types of objects to the function.
"""
class Printer:
    def display(self):
        print("Printing document...")

class Projector:
    def display(self):
        print("Displaying presentation on the wall...")

def show_device_output(device):
     device.display()

# Demonstration
printer = Printer()
projector = Projector()

show_device_output(printer)
show_device_output(projector)

"""
Exercise 12
Create a base class called LibraryItem:
    - Attributes: title (public), _author (protected), __year (private)
    - Method: display_info() to print all three attributes.

- Create two subclasses:
    - Book: adds an attribute genre and overrides display_info()
    - Magazine: adds an attribute issue_number and overrides display_info()

- Print out display info for each of the classes
"""
class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self._author = author
        self.__year = year

    def display_info(self):
        print(f"Title: {self.title}, Author: {self._author}, Year: {self.__year}")

class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def display_info(self):
        print(f"Book → Title: {self.title}, Author: {self._author}, Year: {self._LibraryItem__year}, Genre: {self.genre}")

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Magazine → Title: {self.title}, Author: {self._author}, Year: {self._LibraryItem__year}, Issue: {self.issue_number}")

# Demonstration
b = Book("1984", "George Orwell", 1949, "Dystopian")
m = Magazine("National Geographic", "Various", 2023, 256)
b.display_info()
m.display_info()

"""
Exercise 13
- Create an abstract base class Payment with an abstract method process_payment().
- Subclasses: CreditCardPayment and PayPalPayment.
  Each implements process_payment() differently.

Expected Output:
Processing credit card payment of €120...
Processing PayPal payment of €55...
"""
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self):
        print(f"Processing credit card payment of €{self.amount}...")

class PayPalPayment(Payment):
    def process_payment(self):
        print(f"Processing PayPal payment of €{self.amount}...")

# Demonstration
c = CreditCardPayment(120)
p = PayPalPayment(55)
c.process_payment()
p.process_payment()

"""
Exercise 14
Create an abstract class Employee with:
    - Attributes: name, _salary
    - Abstract method calculate_bonus()

- Subclasses: Manager and Developer
  Each implements calculate_bonus() differently.

- Demonstrate calling calculate_bonus() polymorphically.

Expected Output:
Manager Bonus for Alice: €5000
Developer Bonus for Bob: €2000
"""
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass

class Manager(Employee):
    def calculate_bonus(self):
        print(f"Manager Bonus for {self.name}: €{self._salary * 0.25:.0f}")

class Developer(Employee):
    def calculate_bonus(self):
        print(f"Developer Bonus for {self.name}: €{self._salary * 0.10:.0f}")

employees = [Manager("Alice", 20000), Developer("Bob", 20000)]
for e in employees:
    e.calculate_bonus()

'''
Exercise 15
- Create a class ShoppingCart:
    - Attribute: __items (private, a list)
    - Methods: add_item(item), remove_item(item), and show_cart().

- Allow method chaining (return self after add/remove).
- Demonstrate adding/removing items and displaying the cart.

Expected Output:
Cart: ['Apples', 'Bread']
Cart: ['Bread']
'''

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)
        return self  # method chaining

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        return self

    def show_cart(self):
        print(f"Cart: {self.__items}")

cart = ShoppingCart()
cart.add_item("Apples").add_item("Bread").show_cart()
cart.remove_item("Apples").show_cart()