
def fahrenheit_to_celsius(f):
    return 5 * (f - 32) / 9


f = float(input("Enter temperature in Fahrenheit: "))

celsius = fahrenheit_to_celsius(f)

print(f"{f}°F is equal to {celsius:.2f}°C")
