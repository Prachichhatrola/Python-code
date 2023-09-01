# Q:1 Create a class 2-d vector and use it to create another class representing a 3-d vector.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Example usage:
vector2d = Vector2D(1, 2)
vector3d = Vector3D(3, 4, 5)

print("2D Vector:", vector2d)
print("3D Vector:", vector3d)

# Q:2 Crfeate a class pets from a class animals and further create class dog from pets. add a method bark to class dog.

class Animals:
    def __init__(self, species):
        self.species = species

    def speak(self):
        pass

class Pets(Animals):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

class Dog(Pets):
    def __init__(self, name):
        super().__init__('Dog', name)

    def bark(self):
        return f"{self.name} barks: Woof! Woof!"

# Example usage:
my_dog = Dog('Buddy')
print(f"My pet {my_dog.species} named {my_dog.name} says: {my_dog.bark()}")

# Q:3 Create a class employee and add salary and increment properties to it. 
# write a method SalaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Private variable
        self._increment = None  # Private variable to store increment

    @property
    def salary(self):
        return self._salary

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        if self.salary < 50000:
            self._increment = value
        else:
            self._increment = value * 2

    def SalaryAfterIncrement(self):
        return self.salary + self.increment

# Example usage:
employee1 = Employee("John", 45000)
employee1.increment = 5000
print(f"{employee1.name}'s salary after increment: {employee1.SalaryAfterIncrement()}")

employee2 = Employee("Alice", 60000)
employee2.increment = 5000
print(f"{employee2.name}'s salary after increment: {employee2.SalaryAfterIncrement()}")

# Q:4 Write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return Complex(real_part, imag_part)

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real_part, imag_part)

# Example usage:
num1 = Complex(3, 2)
num2 = Complex(1, 7)

result_addition = num1 + num2
result_multiplication = num1 * num2

print(f"Complex Number 1: {num1}")
print(f"Complex Number 2: {num2}")
print(f"Addition Result: {result_addition}")
print(f"Multiplication Result: {result_multiplication}")

# Q:5 Write a class vector representing a vector of n dimension. overloaded the + and * operator which calculate the sum and the dot product of them.

class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return "(" + ", ".join(map(str, self.components)) + ")"

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for addition")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for dot product")
        result = sum(a * b for a, b in zip(self.components, other.components))
        return result

# Example usage:
vector1 = Vector(1, 2, 3)
vector2 = Vector(4, 5, 6)

# Vector addition
vector_sum = vector1 + vector2
print(f"Vector1 + Vector2 = {vector_sum}")

# Vector dot product
dot_product = vector1 * vector2
print(f"Vector1 * Vector2 (dot product) = {dot_product}")

# Q:6 Write __str__() method to print the vector as follows:
# 7i + 8j +10k
# Assume vector of dimension 3 for this problem.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

# Example usage:
vector = Vector(7, 8, 10)
print(vector)  # Output: 7i + 8j + 10k

# Q:7 Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __len__(self):
        return 3  # 3D vector, so the dimension is always 3

# Example usage:
vector = Vector(7, 8, 10)
print(f"Vector: {vector}")
print(f"Dimension of the Vector: {len(vector)}")
