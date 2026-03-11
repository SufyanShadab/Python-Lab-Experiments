def operations(x, y):
    return x - y, x / y

while True:
    n = int(input("Enter choice:\n1. Perform Operations\n2. Exit\n"))

    if n == 1:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        sub, div = operations(x, y)
        print("Subtraction:", sub)
        print("Division:", div)

    elif n == 2:
        break

    else:
        print("Invalid input")