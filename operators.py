# Arithmetic operators
a = 10
b = 5

addition = a + b  # Addition
print("Addition:", addition)  # Output: 15

subtraction = a - b  # Subtraction
print("Subtraction:", subtraction)  # Output: 5

multiplication = a * b  # Multiplication
print("Multiplication:", multiplication)  # Output: 50

division = a / b  # Division
print("Division:", division)  # Output: 2.0

remainder = a % b  # Modulus (Remainder)
print("Remainder:", remainder)  # Output: 0

exponentiation = a ** b  # Exponentiation
print("Exponentiation:", exponentiation)  # Output: 100000

# Comparison operators
greater_than = a > b  # Greater than
print("Greater than:", greater_than)  # Output: True

less_than = a < b  # Less than
print("Less than:", less_than)  # Output: False

equal_to = a == b  # Equal to
print("Equal to:", equal_to)  # Output: False

not_equal_to = a != b  # Not equal to
print("Not equal to:", not_equal_to)  # Output: True

greater_than_or_equal_to = a >= b  # Greater than or equal to
print("Greater than or equal to:", greater_than_or_equal_to)  # Output: True

less_than_or_equal_to = a <= b  # Less than or equal to
print("Less than or equal to:", less_than_or_equal_to)  # Output: False

# Assignment operators
c = 20
c += 5  # c = c + 5
print("c after addition:", c)  # Output: 25

c -= 3  # c = c - 3
print("c after subtraction:", c)  # Output: 22

c *= 2  # c = c * 2
print("c after multiplication:", c)  # Output: 44

c /= 4  # c = c / 4
print("c after division:", c)  # Output: 5

c %= 3  # c = c % 3
print("c after remainder:", c)  # Output: 2.0

c **= 2  # c = c ** 2
print("c after exponentiation:", c)  # Output: 4.0

# Logical operators
x = True
y = False

logical_and = x and y  # Logical AND
print("Logical AND:", logical_and)  # Output: False

logical_or = x or y  # Logical OR
print("Logical OR:", logical_or)  # Output: True

logical_not = not x  # Logical NOT
print("Logical NOT:", logical_not)  # Output: False


# Membership operators
fruits = ["apple", "banana", "orange"]
a = "apple" in fruits  # Membership check
print("Is apple present:", a)  # Output: True


x = "mango" not in fruits  # Membership check
print("Is mango absent:", x)  # Output: True
