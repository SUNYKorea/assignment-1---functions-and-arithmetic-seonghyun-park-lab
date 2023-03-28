# Name:
# SBUID: 

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

from math import sqrt, tan


def fahrenheit2celsius(fahrenheit): 
   return (float(fahrenheit)-32)*(5/9)

def what_to_wear(celsius):
    if float(celsius) <= -10:
        return print ("Puffy Jacket")
    elif float(celsius) >= -10 and float(celsius) <= 0:
        return print ("Scarf")
    elif float(celsius) >= 0 and float(celsius) <= 10:
        return print ("Sweater")
    elif float(celsius) >= 10 and float(celsius) <= 20:
        return print ("Light Jacket")
    else:
        return print ("T-shirt")

    

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((((x1*y2) + (x2*y3) + (x3*y1)) - ((x1*y3) + (x2*y1) + (x3*y2)))/2) 

def euclidean_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    return euclidean_distance(x1,y1,x2,y2) + euclidean_distance(x2,y2,x3,y3) + euclidean_distance(x3,y3,x1,y1)


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    return deg*(3.14159265359/180)

def apothem(number_sides, length_side):
    return (length_side/(2*tan(deg2rad(180/number_sides))))

def polygon_area(number_sides, length_side):
   return (length_side * number_sides * apothem(number_sides, length_side))/2


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

