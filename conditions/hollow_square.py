
n = int(input("Enter the size of the square: "))

if n < 2:
    print("Please enter a number greater than or equal to 2.")
else:
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")
