# implement a class rectangle with methods to calculate area and perimeter
class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

   

try:
    # get input form user dimensions
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Create Rectangle object
    rect = Rectangle(length, width)

    
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())

except ValueError as ve:
    print("Invalid input:", ve)
except Exception as e:
    print("An error occurred:", e)
