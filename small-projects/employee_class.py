
class Employee:
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary


p = Employee("Zeeshan", "Urdu", 120000)

print(f"Employee's name: {p.name}")
print(f"Employee's language: {p.language}")
print(f"Employee's salary: {p.salary}")
