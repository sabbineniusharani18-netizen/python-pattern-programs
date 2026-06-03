Cubes of Odd Numbers from a List

size = int(input("Enter the number of elements: "))

values = []

# for index in range(size):
    value = int(input(f"Enter value {index + 1}: "))
    values.append(value)

odd_number_cubes = [value ** 3 for value in values if value % 2 != 0]

print("\nEntered List:", values)
print("Cubes of Odd Elements:", odd_number_cubes)#
