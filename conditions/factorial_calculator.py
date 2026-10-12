
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    product = 1

    for i in range(1, n + 1):
        product = product * i

    print(f"The factorial of {n} is {product}.")
