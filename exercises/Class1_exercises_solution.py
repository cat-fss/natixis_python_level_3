'''
SOLUTIONS FOR CLASS 1
'''

# Exercise 1 & 2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def description(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("1984", "George Orwell")
book1.description()


# Exercise 3 & 4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())
print(rect.perimeter())


# Exercise 5 & 6
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def is_passing(self):
        return self.grade >= 10

s1 = Student("Alice", 12)
print(s1.name, s1.grade, s1.is_passing())


# Exercise 7
class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
    
    def get_balance(self):
        return self.balance

acc = BankAccount()
acc.deposit(100)
acc.withdraw(30)
print(acc.get_balance())


# Exercise 8
class Library:
    library_name = "Central Library"
    
    def __init__(self):
        self.books = []
    
    def add_book(self, title):
        self.books.append(title)
    
    def list_books(self):
        print(f"{self.library_name} books: {self.books}")

lib = Library()
lib.add_book("Python 101")
lib.add_book("OOP in Depth")
lib.list_books()


# Exercise 9
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @classmethod
    def from_fahrenheit(cls, f):
        c = (f - 32) * 5/9
        return cls(c)

t1 = Temperature.from_fahrenheit(98.6)
print(t1.celsius, t1.to_fahrenheit())


# Exercise 10
class MathTools:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

print(MathTools.is_even(7))
print(MathTools.is_even(10))


# Exercise 11
my_list = [1, 2, 3]
print(type(my_list))
print(dir(my_list))
my_list.append(4)
print(my_list)


# Exercise 12
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def raise_salary(self, percent):
        self.salary += self.salary * (percent / 100)

emp = Employee("John", 2000)
emp.raise_salary(15)
print(emp.name, emp.salary)


# Exercise 13
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def checkout(self):
        print(f"Total items: {len(self.items)}")

cart = ShoppingCart()
cart.add_item("Milk")
cart.add_item("Eggs")
cart.add_item("Bread")
cart.checkout()


# Exercise 14
class Course:
    school = "Data Academy"
    
    def __init__(self, title):
        self.title = title
        self.students = []
    
    def enroll(self, student):
        self.students.append(student)
    
    def list_students(self):
        print(f"Students in {self.title}: {self.students}")
    
    def count_students(self):
        return len(self.students)

course = Course("Python OOP")
course.enroll("Alice")
course.enroll("Bob")
course.list_students()
print(course.count_students())


# Exercise 15
class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def hire(self, employee):
        self.employees.append(employee)
    
    def list_employees(self):
        for emp in self.employees:
            print(f"{emp.name}: {emp.salary}")
    
    @classmethod
    def from_list(cls, name, emp_list):
        company = cls(name)
        for n, s in emp_list:
            company.hire(Employee(n, s))
        return company
    
    @staticmethod
    def average_salary(employees):
        total = sum(emp.salary for emp in employees)
        return total / len(employees) if employees else 0

company = Company.from_list("TechCorp", [("Alice", 2500), ("Bob", 3000)])
company.list_employees()
print("Average salary:", Company.average_salary(company.employees))
