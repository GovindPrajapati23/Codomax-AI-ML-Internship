# Day 2 - Python Basics

# Variables
name = "Govind Prajapati"
age = 22
cgpa = 8.5
is_student = True

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Student:", is_student)

print("\n----- Data Types -----")
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

print("\n----- Operators -----")
a = 15
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

print("\n----- Conditional Statements -----")
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
else:
    print("Grade: B")

print("\n----- For Loop -----")
for i in range(1, 6):
    print("Number:", i)

print("\n----- While Loop -----")
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

print("\n----- Function -----")

def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

greet("Govind")