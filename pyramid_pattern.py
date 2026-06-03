#Pyramid Pattern Program

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(2 * rows - 1):
        if j == rows - i - 1 or j == rows + i - 1 or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
