#code который определяет функцию для вычисления площади прямоугольника
def calculate_rectangle_area(length, width):   
    area = length * width
    return area

# Example usage:
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_rectangle_area(length, width)
print("The area of the rectangle is:", area)
