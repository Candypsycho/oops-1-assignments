#!/usr/bin/env python
# coding: utf-8

# In[12]:


#1
class bank_account:
    def __init__(self,account_number,account_holder_name,balance):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.balance=0
    def deposit(self,amount):
        print("i would like to deposit amount")
    def withdraw(self,amount_withdraw):
        print('this function will help me to withdraw case')
        
        
        
# objects
x=bank_account(54534555554,'badshah',1000)
x.account_holder_name
x.withdraw(500)


# In[4]:


# 2
class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def calculate_yearly_bonus(self, bonus_percentage):
        bonus = (bonus_percentage / 100) * self.salary
        return bonus

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
# object
syed=Employee(1,'syed mansoor shafi',20000)
syed.calculate_yearly_bonus(10)
syed.display_details()


# In[5]:


# 3
class VehicleRentalSystem:
    def __init__(self):
        # Initialize an empty list to store available vehicles
        self.available_vehicles = []

    def add_vehicle(self, vehicle):
        # Add a vehicle to the list of available vehicles
        self.available_vehicles.append(vehicle)
        print(f"{vehicle} added to available vehicles.")

    def rent_vehicle(self, vehicle_type):
        # Rent a vehicle of the specified type if available
        for vehicle in self.available_vehicles:
            if vehicle.vehicle_type == vehicle_type:
                self.available_vehicles.remove(vehicle)
                print(f"{vehicle} rented successfully.")
                return vehicle
        print(f"No {vehicle_type}s available for rent.")
        return None

    def return_vehicle(self, vehicle):
        # Return a rented vehicle to the list of available vehicles
        self.available_vehicles.append(vehicle)
        print(f"{vehicle} returned successfully.")

    def display_available_vehicles(self):
        # Display the list of available vehicles
        print("Available Vehicles:")
        for vehicle in self.available_vehicles:
            print(vehicle)


class Vehicle:
    def __init__(self, vehicle_id, vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"{self.vehicle_type} (ID: {self.vehicle_id})"


# Create a vehicle rental system
rental_system = VehicleRentalSystem()

# Add vehicles to the system
car1 = Vehicle(vehicle_id=1, vehicle_type="Car")
car2 = Vehicle(vehicle_id=2, vehicle_type="Car")
bike1 = Vehicle(vehicle_id=3, vehicle_type="Bike")

rental_system.add_vehicle(car1)
rental_system.add_vehicle(car2)
rental_system.add_vehicle(bike1)

# Display available vehicles
rental_system.display_available_vehicles()

# Rent a vehicle
rented_vehicle = rental_system.rent_vehicle("Car")

# Display available vehicles after renting
rental_system.display_available_vehicles()

# Return the rented vehicle
rental_system.return_vehicle(rented_vehicle)

# Display available vehicles after returning
rental_system.display_available_vehicles()


# In[6]:


# 4
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        availability = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} (ID: {self.book_id}, {availability})"


class Library:
    def __init__(self):
        # Initialize an empty list to store books
        self.books = []

    def add_book(self, book):
        # Add a book to the library
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def borrow_book(self, book_id):
        # Borrow a book with the specified ID if available
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.is_available = False
                print(f"Book '{book.title}' borrowed successfully.")
                return book
        print(f"Book with ID {book_id} not available for borrowing.")
        return None

    def return_book(self, book):
        # Return a borrowed book to the library
        if book in self.books:
            book.is_available = True
            print(f"Book '{book.title}' returned successfully.")
        else:
            print("Invalid book return. Book not found in the library.")

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(book)
library = Library()
book1 = Book(book_id=1, title="curfewed nights", author="basharat peer")
book2 = Book(book_id=2, title="the collaborator", author="mirza waheed")
book3 = Book(book_id=3, title="the half mother", author="shahnaz bashir")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_available_books()
borrowed_book = library.borrow_book(2)
library.display_available_books()
library.return_book(borrowed_book)
library.display_available_books()


# In[8]:


#5
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}, Price: {self.price}, Quantity: {self.quantity})"


class InventorySystem:
    def __init__(self):
        # Initialize an empty list to store products
        self.products = []

    def add_product(self, product):
        # Add a product to the inventory
        self.products.append(product)
        print(f"Product '{product.name}' added to the inventory.")

    def update_quantity(self, product_id, new_quantity):
        # Update the quantity of a product with the specified ID
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = new_quantity
                print(f"Quantity of product '{product.name}' updated to {new_quantity}.")
                return product
        print(f"Product with ID {product_id} not found in the inventory.")
        return None

    def display_available_products(self):
        # Display the list of available products
        print("Available Products:")
        for product in self.products:
            print(product)
# Create an inventory system
inventory_system = InventorySystem()
# Add products to the inventory
product1 = Product(product_id=1, name="Laptop", price=800, quantity=10)
product2 = Product(product_id=2, name="Smartphone", price=500, quantity=20)
product3 = Product(product_id=3, name="Headphones", price=50, quantity=30)

inventory_system.add_product(product1)
inventory_system.add_product(product2)
inventory_system.add_product(product3)

# Display available products
inventory_system.display_available_products()

# Update product quantity
inventory_system.update_quantity(product_id=2, new_quantity=15)

# Display available products after updating quantity
inventory_system.display_available_products()


# In[21]:


#6
import math
class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius**2
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def calculate_area(self):
        return 0.5 * self.base * self.height
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
r = 7
circle = Circle(r)
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()
print("Radius of the circle:", r)
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)
l = 5
w = 7
rectangle = Rectangle(l, w)
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()
print("\nRectangle: Length =", l, " Width =", w)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)
base = 5
height = 4
s1 = 4
s2 = 3
s3 = 5
print("\nTriangle: Base =", base, " Height =", height, " side1 =", s1, " side2 =", s2, " side3 =", s3)
triangle = Triangle(base, height, s1, s2, s3)
triangle_area = triangle.calculate_area()
triangle_perimeter = triangle.calculate_perimeter()
print("Triangle Area:", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)


# In[14]:


#7
class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def calculate_average_grade(self):
        if not self.grades:
            return 0  # Return 0 if there are no grades to avoid division by zero
        return sum(self.grades) / len(self.grades)

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Grades:", self.grades)
        print("Average Grade:", self.calculate_average_grade())
# Create a student instance
student1 = Student(student_id=1, name="syed mansoor", grades=[85, 90, 78, 92, 88])

# Display student details
student1.display_details()


# In[16]:


#8
class Email:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.sent = False

    def send_email(self):
        print(f"Email sent from {self.sender} to {self.recipient}")
        self.sent = True

    def display_details(self):
        print("Sender:", self.sender)
        print("Recipient:", self.recipient)
        print("Subject:", self.subject)
        print("Body:", self.body)
        print("Sent:", "Yes" if self.sent else "No")
# instance
email1 = Email(sender="syed@example.com", recipient="aakash@example.com", subject="Meeting", body="Hello syed, let's meet tomorrow.")
email1.display_details()
email1.send_email()
email1.display_details()


# In[18]:


#9
class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, post_content):
        post = {"content": post_content, "author": self.username}
        self.posts.append(post)
        print(f"Post added by {self.username}")

    def display_posts(self):
        print(f"Posts by {self.username}:")
        for post in self.posts:
            print(f"{post['author']}: {post['content']}")

    def search_posts(self, keyword):
        matching_posts = [post for post in self.posts if keyword.lower() in post['content'].lower()]
        print(f"Posts containing '{keyword}' by {self.username}:")
        for post in matching_posts:
            print(f"{post['author']}: {post['content']}")

profile1 = SocialMediaProfile(username="syed mansoor")
profile1.add_post("Enjoying a sunny day!")
profile1.add_post("Trying out a new recipe for dinner.")
profile1.add_post("Just finished a good book.")
profile1.display_posts()
profile1.search_posts(keyword="recipe")


# In[19]:


#10
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date=None):
        new_task = {"task": task, "due_date": due_date, "completed": False}
        self.tasks.append(new_task)
        print(f"Task '{task}' added to the ToDo list.")

    def mark_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Task '{self.tasks[task_index]['task']}' marked as completed.")
        else:
            print("Invalid task index.")

    def display_pending_tasks(self):
        print("Pending Tasks:")
        for index, task in enumerate(self.tasks):
            if not task["completed"]:
                print(f"{index + 1}. {task['task']} (Due Date: {task['due_date'] or 'Not specified'})")
todo_list = ToDoList()
todo_list.add_task("Finish project", due_date="2023 13 12")
todo_list.add_task("play cricket")
todo_list.add_task("play pubg", due_date="2023-12-14")
todo_list.display_pending_tasks()
todo_list.mark_as_completed(1)
todo_list.display_pending_tasks()


# In[ ]:




