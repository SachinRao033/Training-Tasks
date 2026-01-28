#a= int(input("Enter first number: "))
#b= int(input("Enter second number: "))

#Arithmetic Operations:
   #Simple calculations
'''
print ("Add      :", a+b)
print ("Subtract :", a-b)
print ("Multiply :", a*b)
print ("Divide   :", a/b)
print ("Modulus  :", a%b)
'''
    #Total and average calculation
'''
total = a + b
average = total / 2
print ("Total :", total)
print ("Average :", average)
'''



#Comparison (Relational) Operators:
    #Age validation
'''
a=int(input("Enter the Age: "))
if a >= 18:
    print ("He is eligible for vote...!")
else:
    print ("He is not eligible for vote...!")
'''
    #Number comparison

'''a=int(input("Enter the 1st number:- "))
b=int(input("Enter the 2nd number:- "))
if a > b:
    print ("1st number is greater than 2nd number")
elif a <= b:
    print ("2nd number is greater than 1st number")
elif a == b:
    print ("Both numbers are equal")
else:
    print ("Both numbers are not equal")'''

    #Demonstration of all comparison operators
'''
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
print ("Is a equal to b? :", a==b)
print ("Is a not equal to b? :", a!=b)
print ("Is a greater than b? :", a>b)
print ("Is b less than a? :", b<a)
print ("Is a greater than or equal to b? :", a>=b)
print ("Is b less than or equal to a? :", b<=a)
'''



#Logical Operators:
    #Age Eligibility and Marks Validation
'''
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if age >= 18 and marks >= 50:
    print("Eligible and Pass")
else:
    print("Not Eligible and Fail")
'''


#Assignment Operators
'''
x = int(input("Enter initial value of x: "))
print("Initial value:", x)

x += 5
print("After += :", x)

x -= 3
print("After -= :", x)

x *= 2
print("After *= :", x)

x /= 4
print("After /= :", x)

x %= 3
print("After %= :", x)
'''


#Bitwise Operators
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Bitwise AND (&):", a & b)
print("Bitwise OR (|):", a | b)
print("Bitwise XOR (^):", a ^ b)
print("Bitwise NOT (~) of a:", ~a)
print("Bitwise NOT (~) of b:", ~b)
print("Left Shift (a << 2):", a << 2)
print("Right Shift (b >> 2):", b >> 2)
'''

#Range of numbers 0-100 print numbers divisible by 3 or 5, if divisible by both print 'py'

'''for i in range(1,101):
  if i%3!=0 and i%5!=0:
    print(i ,end=' ')
  elif i%3==0 and i%5==0:
    print("py" , end=' ')
    continue
else:
    print("" , end=' ')'''


#slicing of list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original List:", my_list )
print("Sliced List (Index 2 to 5):", my_list[2:6])
print("Sliced List (From Start to Index 4):", my_list[:5])
print("Sliced List (From Index 5 to End):", my_list[5:])
print("Sliced List (Every 2nd Element):", my_list[::2])
print("Reversed List:", my_list[::-1])



#Print first 10 natural numbers using while loop
'''i=1
while i<=10:
    print(i , end=' ')
    i+=1
print()
'''


#Print first 10 natural numbers using for loop
'''for i in range(1,11):
    print(i , end=' ')'''


#Find the grade of a student based on marks obtained
'''marks=int(input("Ener Your Mark:"))
if 90<=marks<=100:
    print("O")
elif 80<=marks<=89:
    print("A+")
elif 70<=marks<=79:
    print("A")
elif 60<=marks<=69:
    print("B")
elif 50<=marks<=59:
    print("C")
elif marks>100 or marks<0:
    print("Invalid")
else:
  print("Fail")'''


# Nested If-Else
'''a = int(input("Enter a number: "))
if a>10:
     if a>=15:
         print("Very High")
     else:
         print("High")
else:
     if a<=5:
         print("Very Low")
     else:
         print("Low")
'''


# Program to print M pattern using loops
'''size = int(input("Enter the dimension: "))
for row in range(size):
    for col in range(size):
        if (
            col == 0 or col == size - 1 or
            (row == col and row < size // 2 + 1) or
            (row + col == size - 1 and row < size // 2 + 1)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

# Program to print pyramid pattern
'''rows = int(input("Enter number of rows: "))
for i in range(rows):

    print(" " * (rows - i - 1) + "* " * (i + 1))'''


# Program to print inverted pyramid pattern
'''rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)'''

