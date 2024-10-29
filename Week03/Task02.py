import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector3D({self.x},{self.y},{self.z})"

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

        return Vector3D(self.x + other, self.y + other, self.z + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self = self.__add__(other)

        return self

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)

        return Vector3D(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        self = self.__mul__(other)

        return self

    def __eq__(self, other):
        return (
            isinstance(other, Vector3D)
            and self.x == other.x
            and self.y == other.y
            and self.z == other.z
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __abs__(self):
        return math.sqrt(self.x**2 +  self.y**2 + self.z**2)

    def __getattr__(self, name):
        match (name):
            case "X":
                return self.x
            case "Y":
                return self.y
            case "Z":
                return self.z
            case _:
                return None

    def __setattr__(self, name, value):
        match (name):
            case "X" | "x":
                object.__setattr__(self, "x", value)
            case "Y" | "y":
                object.__setattr__(self, "y", value)
            case "Z" | "z":
                object.__setattr__(self, "z", value)
            case _:
                object.__setattr__(self, name, value)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

# Test the Vector3D class
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

# Test __str__ and __repr__
print(repr(v1))  # Expected: Vector3D(1, 2, 3)
print(str(v1))  # Expected: (1, 2, 3)

# Test addition with another vector
v3 = v1 + v2
print(v3)  # Expected: Vector3D(5, 7, 9)

# Test addition with a scalar
v4 = v1 + 3
print(v4)  # Expected: Vector3D(4, 5, 6)

# Test in-place addition with another vector
v1 += v2
print(v1)  # Expected: Vector3D(5, 7, 9)

# Test multiplication with another vector
v5 = v1 * v2
print(v5)  # Expected: Vector3D(20, 35, 54)

# Test multiplication with a scalar
v6 = v1 * 2
print(v6)  # Expected: Vector3D(10, 14, 18)

# Test in-place multiplication
v1 *= 2
print(v1)  # Expected: Vector3D(10, 14, 18)

# Test equality and inequality
print(v1 == v6)  # Expected: True
print(v1 != v2)  # Expected: True

# Test absolute value (magnitude)
print(abs(v1))  # Expected: 25.45584412271571 (or similar)

# Test attribute access with X, Y, Z
print(v1.X)  # Expected: 10
print(v1.Y)  # Expected: 14
print(v1.Z)  # Expected: 18

# Test iteration
