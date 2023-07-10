# The user to enter the first number
number1 = (input("Enter the first number: "))

# The user to enter the second number
number2 = (input("Enter the second number: "))

# Print the initial values of the two numbers
print("Before swapping:")
print("Number 1:", number1)
print("Number 2:", number2)

# Swap the values of the two numbers using a temporary variable
temp = number1
number1 = number2
number2 = temp

# Print the swapped values of the two numbers
print("After swapping:")
print("Number 1:", number1)
print("Number 2:", number2)
