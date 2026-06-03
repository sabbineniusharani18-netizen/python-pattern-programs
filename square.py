#Squares of Numbers

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    square = number * number
    print(f"Square of {number} = {square}")
