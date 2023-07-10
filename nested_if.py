height = int(input("What is your height in feet? "))
if height >= 3:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age <= 18:
        print("Pay 250")
    elif age <= 25:
        print("Pay 500")
else:
    print("Pay 600")
