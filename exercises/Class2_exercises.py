'''
Class 1 Exercises - Python L3
'''

'''
Exercise 1
- Create a class named "Animal" with "age" and "name" attributes. Age should default to 0 and be protected.
- Add a method called describe() to the Animal class that returns "This animal is called [name] and is [age] years old."
- Call describe()
'''

'''
Exercise 2
Create a method in the Animal class called celebrate_birthday that increases age by 1 and calls describe(). Call the celebrate_birthday() method.

Expected Output
"This animal is called [name] and is [age] years old."
'''

'''
Exercise 3
Create a class Person with attributes: name, age (protected), and personal_id (private) and method introduce, that returns "Hello, my name is [name] and I am [age] years old."
'''

'''
Exercise 4
Create subclasses Student and Teacher that inherit from Person. Each one should add a new attribute:
Student: student_id
Teacher: subject
'''

'''
Exercise 5
Give each subclass its own version of introduce(), showing their specific role.
'''

'''
Exercise 6
Write a function introduce_person(person) that calls person.introduce() for any object that has that method.
'''

'''
Exercise 7
- Add a private attribute __email to Person.
- Create a method show_email() to display it safely.
- Try to print email from outside the class without show_email().
'''

'''
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
'''


'''
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
'''

'''
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
'''

'''
Exercise 11
- Create two unrelated classes: Printer and Projector.
    - Each should have a method display() that returns an appropriate message.

- Create a function show_device_output(device) that calls the display() method.
- Demonstrate polymorphism by passing both types of objects to the function.
'''


'''
Exercise 12

Create a base class called LibraryItem:
    - Attributes: title (public), _author (protected), __year (private)
    - Method: display_info() to print all three attributes.

- Create two subclasses:
    - Book: adds an attribute genre and overrides display_info()
    - Magazine: adds an attribute issue_number and overrides display_info()

- Print out display info for each of the classes
'''

'''
Exercise 13
- Create an abstract base class Payment with an abstract method process_payment().
- Subclasses: CreditCardPayment and PayPalPayment.
  Each implements process_payment() differently.

Expected Output:
Processing credit card payment of €120...
Processing PayPal payment of €55...
'''

'''
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
'''

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