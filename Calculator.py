def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1 is Add")
print("2 is Subtract")
print("3 is Multiply")
print("4 is Divide")

while True:
    choice= input("Enter choice(1/2/3/4):")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Type in your first number"))
        num2 = float(input("Type in your second number"))

        if choice == '1':
            print (num1, "+", num2, '=', add(num1, num2))

        elif chice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            break
        else:
            print("That is wrong")
