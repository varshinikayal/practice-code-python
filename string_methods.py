#capitalizes the first letter of a string and converts the rest of the characters to lowercase
print("hello, world!".capitalize())

#converts all characters in a string to lowercase
print ('Hello World'.lower())

#converts all characters in a string to uppercase
print("hello world".upper())

# Centers the string "Python" within a width of 20 characters, padding it with spaces on both sides
print("Python".center(20))

# Splits the string "3/2/1995" at each occurrence of the forward slash ('/') and returns a list of substrings
print('3/2/1995'.split('/'))

# Replaces all occurrences of the forward slash ('/') with a hyphen ('-') in the string "3/2/1995"
print('3/2/1995'.replace('/', '-'))

# Finds the index of the first occurrence of the substring 'R' within the string "HELLO WORLD"
print("HELLO WORLD".index('R'))

# Counts the number of occurrences of the letter 'l' in the string "hello world"
print("hello world".count('l'))

# Checks if the string "helloworld" is entirely in lowercase
print("helloworld".islower())

# Checks if the string '12234' contains only numeric characters
print('12234'.isnumeric())

# Checks if the string "abc123" is alphanumeric, meaning it contains only letters and numbers
print("abc123".isalnum())

