area_square= input("What is the length of a side of a square?")
print("The area of the square is:", float(area_square)**2)
leng_rect= input("Length of a rectangle?")
width_rect= input("Width of rectangle?")
print("The area of the rectangle is:", float(leng_rect)*float(width_rect))
import math
pi= math.pi
area_circle= input("Radius of circle?")
print("Area of circle is:", pi * float(area_circle)**2)
all_value= input("A single length value?")
print("Area of square:", float(all_value)**2)
print("Area of circle:", pi* float(all_value)**2)
print("Volume of cube:", float(all_value)**3)
print("Volume of sphere:", int(4/3)*pi*float(all_value)**3)
