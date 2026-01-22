# Program to print M pattern using loops
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
    print()



'''
size = int(input("Enter the dimension: "))

for row in range(size):
    for col in range(size):
        if (
            col == 0 or
            col == size - 1 or
            (row == col and row <= size // 2) or
            (row + col == size - 1 and row <= size // 2)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''