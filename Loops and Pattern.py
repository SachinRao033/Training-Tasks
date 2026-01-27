'''# Program to print M pattern using loops
size = int(input("Enter the dimension: "))

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


marks=int(input("Ener Your Mark:"))
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
  print("Fail")

# Nested If-Else
# a = int(input("Enter a number: "))
#if a>10:
#     if a>=15:
#         print("Very High")
#     else:
#         print("High")
# else:
#     if a<=5:
#         print("Very Low")
#     else:
#         print("Low")