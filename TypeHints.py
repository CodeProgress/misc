class Circle:
    PI = 3.14159  # type: float

    def area_of_circle(self, radius: float) -> float:
        return self.PI * radius**2


def power(base: int, exp: int) -> int:
    return base**exp


def square_root(num: int) -> float:
    return num**.5

print(power(2, 6))
print(square_root(64))

x = square_root(16)
print(power(x, 3))  # type check warning
