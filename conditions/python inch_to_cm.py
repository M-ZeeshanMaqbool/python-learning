
def inches_to_cm(inches):
    centimeters = inches * 2.54
    return centimeters


inches = float(input("Enter a value in inches: "))
centimeters = inches_to_cm(inches)

print(f"{inches} inches = {centimeters:.2f} cm")
