
with open("myfile.txt", "r") as f:
    data = f.read()

if "twinkle" in data:
    print("Twinkle is available")
else:
    print("Twinkle is not available")

