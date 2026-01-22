a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic Operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Total and Average
total = a + b
average = total / 2

print("Total:", total)
print("Average:", average)




# Assignment Operators
x = 10
print("Initial value:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)





# Comparison Operators
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

print("Marks > 50:", marks > 50)
print("Marks < 50:", marks < 50)
print("Marks == 50:", marks == 50)

print("Age >= 18 (Eligible):", age >= 18)
print("Age < 18 (Not Eligible):", age < 18)





# Logical Operators
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

# AND condition
if marks >= 40 and attendance >= 75:
    print("Student Passed")
else:
    print("Student Failed")

# OR condition
if marks >= 90 or attendance >= 95:
    print("Excellent Performance")

# NOT condition
is_failed = marks < 40
print("Is student failed:", not is_failed)
