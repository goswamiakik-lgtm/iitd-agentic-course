''' 
#? OOPS Concept 
Classes 
Objects
Methods 
Constructor 
Inheritance
Method overriding 
Super() method 

#? Error Handling
Exception
try catch block
finally 
Custom Exception
'''

#? Classes 
''' 
Bike -> Name = Royal Enfield 
        mileage = 
        gear = 
        color = 
function 
```
def function_name():
    # block code for function

function_name()
```

now we have to define a class
```
class Bike:
    name # name of the bike
    mileage 
    gear 
    color
```
'''

# class Bike:
#     # Attributes of Bike class
#     name: str = "Royal Enfield"
#     mileage: int = 10 
#     gear: int = 5 
#     color: str = "Black"

# # to intialize a class we have to store (information) inside a variable (object)

# bike = Bike() # intialization of class object 

# '''
# type() 
# '''
# print(f"Datatype of `bike` object: {type(bike)}")

# print(f"name of the bike: {bike.name}") # . operator helps you to access attributes of the class (Bike) 
# print(f"Number of gears in my bike: {bike.gear}")


# class Bike:
#     # Attributes of Bike class
#     name: str = "Royal Enfield"
#     mileage: int = 10 
#     gear: int = 5 
#     color: str = "Black"

#     def is_in_operation(self, x, y) -> bool: # function -> method  typehint
#         print("-----")
#         print(self)
#         print("-----")
#         print(x) 
#         print(y)
#         return True

# # to intialize a class we have to store (information) inside a variable (object)

# bike = Bike() # intialization of class object 

# if bike.is_in_operation(2,3):
#     print(f"{bike.name} is currently in operation")
# else:
#     print("Not Available nowadays")


'''
I have a room of length = 10.0 and breadth = 14.0 and height = 5.0 now design a class for me 
and also mention property to calculate area and volumne of the room
'''

'''
Constructor
'''

# class Room:
#     def __init__(self, length, breadth, height):
#         self.length = length 
#         self.breadth = breadth 
#         self.height = height
    
#     def calculate_area(self):
#         return self.length * self.breadth

#     def calculate_volume(self):
#         return self.length * self.breadth * self.height 
    

# length = float(input("Enter the length: "))
# breadth = float(input("Enter the breadth: "))
# height = float(input("Enter the height: "))
# room = Room(length, breadth, height)
# print(room.calculate_area())
# print(room.calculate_volume())

#? Inheritance 


''' 
class A is inherting class B -> class A(B)

class B -> parent class 
is-a relationship
class A -> child class

class B -> parent 

class A -> can access all attribute and methods of parent class
'''

# class Animal():
#     name = "Akeal"
#     def eat(self):
#         print("I can eat")
    
# class Dog(Animal):
#     name = "Rohu"
#     def display(self):
#         print(f"My name is {self.name}")
#         print(f"{super().name}")

# labrador = Dog()
# print(labrador.name) 
# labrador.display()


#? Classes, Objects, Inheritance, super(), Constructor 

''' 
OOP Design of Company 

-> Employee (Base Class) -> common properties
-> Manager (Child) : Employee -> manage team
-> Developer (Child) : Employee -> has programming language
-> Department -> contains employees data (composition) 
'''

# class Employee:
#     def __init__(self, emp_id: int, name: str, salary: int):
#         self.emp_id = emp_id 
#         self.name = name 
#         self.salary = salary 
    
#     def display_info(self):
#         return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"

#     def calculate_bonus(self):
#         return self.salary * 0.10 
    
# class Manager(Employee):
#     def __init__(self, emp_id: int, name: str, salary: int, team_size: int):
#         super().__init__(emp_id, name, salary) 
#         self.team_size = team_size 
    
#     def display_info(self):
#         base_info = super().display_info()
#         return f"{base_info}, Team Size: {self.team_size}"
    
#     def calculate_bonus(self):
#         return self.salary * 0.20
    
# class Developer(Employee):
#     def __init__(self, emp_id: int, name: str, salary: int, language: str):
#         super().__init__(emp_id, name, salary) 
#         self.language = language 
    
#     def display_info(self):
#         base_info = super().display_info() 
#         return f"{base_info}, Language: {self.language}"
    
#     def calculate_bonus(self):
#         return self.salary * 0.15 
    
# class Department:
#     def __init__(self, dept_name):
#         self.dept_name: str = dept_name 
#         self.employees: list[Employee] = []
    
#     def add_employee(self, emp: Employee):
#         self.employees.append(emp)
    
#     def show_all_employees(self):
#         print(f"Department name: {self.dept_name}")
#         for emp in self.employees:
#             print(emp.display_info()) 
        
#     def total_salary(self):
#         sum = 0 
#         for emp in self.employees:
#             sum += emp.salary 
#         return sum 

# if __name__ == '__main__': # main execution flow
#     # Creation of Employee Objects
#     emp1 = Employee(1, "Alice", 50000)
#     emp2 = Manager(2, "Bob", 80000, 5)
#     emp3 = Developer(3, "Charlie", 60000, "Python")

#     # Create Department
#     dept = Department("IT")

#     # Add Employees
#     dept.add_employee(emp1)
#     dept.add_employee(emp2)
#     dept.add_employee(emp3)

#     # show employees data 
#     dept.show_all_employees()

#     # Show Bonuses 
#     print("-----Bonuses-------")
#     for emp in dept.employees:
#         print(f"{emp.name} Bonus: {emp.calculate_bonus()}")

#     # Total Salary 
#     print(f"Total Department Salary: {dept.total_salary()}")


''' 
a   : public
_a  : protected 
__a : private
'''

# class A:
#     c = 12         # public attribute
#     __a = "Mayank" # private attribute
#     _b = "Aakash"  # protected attribute
#     def display(self):
#         return self.__a 

# class B(A):
#     def display(self):
#         return self.c # Aakash

# a = A()
# print(a)

#? Exception Handling 

# IndexError
# a = [1,2,3,4]
# print(a[5])

# ZeroDivisionError
# a = 7/0 
# print(a)

# NameError
# print(f())
# if __name__ == '__main__':
#     def f():
#         return "Mayank"

# AttributeError
# class A:
#     pass 
# obj = A() 
# print(obj.a)

#? Handling Exception 

# try:
#     a = 70/0 
#     print(a)
# except:
#     print("ZeroDivisionException Occured")

# try:
#     x = int(input("Number: "))
#     y = 10/x
#     print(y)
# except ZeroDivisionError:
#     print("Cant' divide with 0")
# finally:
#     y = 10/0
#     print(y)


#? Custom Exception 

# class InvalidAgeException(Exception):
#     """Raise when the input age value is less than 18"""
#     pass 

# number = 18 

# try:
#     input_value = int(input("Enter the age: "))
#     if input_value < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to vote")
# except InvalidAgeException:
#     print("Exception occured: Invalid age for voting")

