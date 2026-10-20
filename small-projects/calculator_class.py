
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of {self.n} is {self.n ** 2}")

    def cube(self):
        print(f"Cube of {self.n} is {self.n ** 3}")

    def square_root(self):
        print(f"Square root of {self.n} is {self.n ** 0.5}")


a = Calculator(8)
a.square()
a.cube()
a.square_root()
