from Functions import Add, Sub, Mul, Div
print("Howdy! Welcome to my 4 function calculator")

error = True
while error:
    function = input("Would you like to add(a), subtract(s), multiply(m), or divide(d)? ")
    if function.lower() == "a":
        num1 = int(input("Enter your first number "))
        num2 = int(input("Enter your second number "))
        print("your result is:", Add(num1, num2))

    elif function.lower() == "s":
        num1 = int(input("Enter your first number "))
        num2 = int(input("Enter your second number "))
        print("your result is:", Sub(num1, num2))

    elif function.lower() == "m":
        num1 = int(input("Enter your first number "))
        num2 = int(input("Enter your second number "))
        print("your result is:", Mul(num1, num2))

    elif function.lower() == "d":
        num1 = int(input("Enter your first number "))
        num2 = int(input("Enter your second number "))
        print("your result is:", Div(num1, num2))

    else:
        error = False