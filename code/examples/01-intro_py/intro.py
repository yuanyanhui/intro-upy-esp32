"""
Python Tutorial

- Hello world
- Python as a caculator
- variables
- strings
- arithmetic operators
- comparison operators 
- if statements
- logical operators
- lists
- tuples
- dictionaries
- loops
- functions
- classes
- modules
"""

# Ctrl-l    Clear command line
# Ctrl-c    Interrupt current Python command
# Ctrl-d    Exit Python session
# up and down arrow to cycle through past commands


# ---------------- Hello World ----------------
print("Hello World!")
name = input("What's your name? ")
print("Hello ", name)


# ---------------- Python as caculator ----------------
# Type on command line
# 1+2
# 0.3*5
# 4**2


# ---------------- variables ----------------
# distance = 10         # integer, type()
# speed = 4.9           # float
# message = 'Hello'     # string
# is_cool = True        # boolean  True/False


# ---------------- strings ----------------
# We can define strings using single (' ') or double (" ") quotes.
# To define a multi-line string, use triple quotes (""").
# empty_string = ''  # empty string
# course = 'Python Tutorial'
# print(course[0])       # first character
# print(course[1])       # second character
# print(course[-1])      # first character from the end
# print(course[-2])      # second character from the end
# print(course[1:5])     # string slicing (5th not included)

# string concatenation
# message = 'Hello ' + 'World'
# print(message)

# formatted strings
# name = 'Python'
# message = f'Hello {name}!'
# print(message)

# string methods/functions
# message.upper()               # to convert to uppercase
# message.lower()               # to convert to lowercase
# message.find('P')             # index of first occurrence of 'P'
# message.replace('P', 'Q')
# is_contained = 'Python' in message     # in operator


# ---------------- arithmetic operators ----------------
# +, -, *, /, //, %, **
# print(5/2)         # / returns a float
# print(5//2)        # // returns an int
# print(5%2)         # % returns the remainder
# print(5**2)        # x**y returns x to the power of y


# ---------------- comparison operators ----------------
# a > b
# a >= b (greater than or equal to)
# a < b
# a <= b
# a == b (equal)
# a != b (not equal)


# ---------------- if statements ----------------
# age = 15
# 
# if age < 18:                # colon
#     print("Too young!")     # indentation
#     print("No pass!")
# elif age > 30:
#     print("Too old!")
#     print("No pass!")
# else:
#     print("Right age!")
#     print("Pass!")

    
# ---------------- logical operators ----------------
# and, or, not
# is_hot = False
# is_cold = False
# if not is_hot and not is_cold:
#     print("beautiful day")
#     
# if is_hot or is_cold:
#     print("not a good day")

    
# ---------------- list ----------------
# empty_list = []    # empty list
# numbers = [1, 2, 3, 4, 5]
# numbers[0]         # first item
# numbers[1]         # second item
# numbers[-1]        # first item from the end
# numbers[-2]        # second item from the end
# numbers[:]         # returns a copy of the whole list
# numbers[::2]       # returns [1, 3, 5]
# numbers[::-1]      # reverse the list 

# list methods/functions
# numbers.append(6)         # adds 6 to the end
# numbers.insert(0, 6)      # adds 6 at index position of 0
# numbers.remove(6)         # removes 6
# numbers.pop()             # removes the last item
# numbers.clear()           # removes all the items
# numbers.index(8)          # index of first occurrence of 8
# numbers.sort()            # sorts the list
# numbers.reverse()         # reverses the list
# numbers.copy()            # returns a copy of the list


# ---------------- tuple ----------------
# tuples are like lists, but immutable (read-only).
# coordinates = (1, 2, 3)
# x, y, z = coordinates      # unpack a list or a tuple
# coordinates[1] = 0         # error


# ---------------- dictionary ----------------
# We use dictionaries to store key/value pairs.
# student = {
# "name": "John Smith",      # key = "name", value = "John Smith"
# "age": 20,
# "is_registered": True
# }

# student["name"]            # "John Smith"
# student.get("name")        # "John Smith"
# student["name"] = "Steve Jobs"


# ---------------- loops ----------------
# while loop
# i = 1
# while i < 5:
#     print(i)
#     i += 1

# for loop
# range(5)         # 0, 1, 2, 3, 4
# list(range(5))   # [0, 1, 2, 3, 4]
# range(1, 5)      # 1, 2, 3, 4
# range(1, 5, 2)   # 1, 3
# for i in range(1, 5):
#     print(i)

# in operator
# for c in "hello world!":
#     print(c)
# 
# numbers = [1, 2, 3, 4, 5]    # list
# for n in numbers:
#     print(n)
# 
# coordinates = (1, 2, 3)      # tuple
# for n in coordinates:
#     print(n)
#     
# student = {                  # dictionary
# "name": "John Smith",
# "age": 20,
# "is_registered": True
# }
# for key in student:
#     print(key, student[key])
    
    
# ---------------- functions ----------------
# def greet_user(name):      
#     print(f"Hi {name}")      # return None
#     
# greet_user("John")
# 
# def square(number):
#     return number * number   # return value
# 
# result = square(2)
# print(result) # prints 4


# ---------------- classes ----------------
# Classes are user-defined data types.
# An object consists of attributes (properties, data) and behavior (operations).
# Functions of a class are called methods.
# A class is a blueprint, an object is an instance of a class.

# class Point:
#  def __init__(self, x, y):  # a special method called constructor.
#      self.x = x
#      self.y = y
#  def get_coord(self):       
#      return self.x, self.y
#  def set_coord(self, x, y):
#      self.x = x
#      self.y = y
#  def distance(self, point):
#      return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5   
    
# p1 = Point(0, 0)  # An object is an instance of a class.
# p2 = Point(1, 1)
# print(p1.get_coord())
# p2.set_coord(3, 4)
# print(p2.get_coord())
# print("Distance between p1 and p2 is: ", p1.distance(p2))

# Class inheritance
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def set_name(self, name):
#         self.name = name
#     def get_name(self):
#         return self.name
#         
# class Student(Person):          # Student inherits from Person
#     def __init__(self, name, major):
#         Person.__init__(self, name)
#         self.major = major
#         self.grades = {}        # empty dict
#     
#     def get_major(self):
#         return self.major
#         
#     def add_grades(self, course, grade):
#         self.grades[course] = grade
# 
#     def get_grades(self):
#           return self.grades
#        
# s1 = Student("Xiao Wang", "Mechanical Engineering")
# s1.add_grades("Programming", 100)
# s1.add_grades("Robotics", 95)
# 
# name = s1.get_name()          # method inherited from Person class
# major = s1.get_major()
# grades = s1.get_grades()
# 
# print(" Student information ")
# print(f" Name: {name}\n Major: {major}\n Grades: {grades} ")

# ---------------- modules ----------------
# A module is a file with some Python code.
# importing the entire time module
# import time         # dir() to list all functions in a module
# print("Start sleeping for 5 seconds")
# time.sleep(5)
# print("Sleep ended")

# importing one function from the time module
# from time import sleep 
# print("Start sleeping for 5 seconds")
# sleep(5)
# print("Sleep ended")
