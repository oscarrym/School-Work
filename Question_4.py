
from inspect import Parameter


def calculate_area(Length, Width):
    area = Length * Width
    return(area)

def calculate_perimeter(Length, Width):
    perimeter = (Length * 2) + (Width * 2)
    return(perimeter)
    
def print_result(area, perimeter):
    print("The area of the rectangle is:",area)
    print("The perimeter of the rectangle is",perimeter)

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = calculate_area(length,width)
perimeter = calculate_perimeter(length,width)  

print_result(area,perimeter)