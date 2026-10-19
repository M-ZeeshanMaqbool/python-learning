
from pathlib import Path


def generate_table(n):
    table = ""

    for i in range(1, 11):
        table += f"{n} × {i} = {n * i}\n"

    folder = Path("tables")
    folder.mkdir(exist_ok=True)

    with open(folder / f"table_{n}.txt", "w", encoding="utf-8") as f:
        f.write(table)


for i in range(2, 21):
    generate_table(i)

print("Multiplication tables from 2 to 20 have been created!")
