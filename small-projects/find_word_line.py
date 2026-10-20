
with open("find.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

lineno = 1

for line in lines:
    if "python" in line.lower():
        print(f"Python is available on line {lineno}")
        break
    lineno += 1
else:
    print("Python was not found.")
