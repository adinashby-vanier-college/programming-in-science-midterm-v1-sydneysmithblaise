import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = round(math.pi * (radius **2), 2)
    return area



# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n < 4:
        return "The triangle height should be at least 4."
    
    result = ""

    for i in range(n):
        for j in range(i + 1):
            if i == 0 or i == n -1:
                result += "*"
            elif j == 0 or j == i:
                result += "*"
            else:
                result += " "
                    
        if i < n - 1:
            result += "/n"
    
    return result

                  

# Q3: Inverted Pyramid
def inverted_pyramid(n):
        if n < 3:
            return "The pyramid height should be at least 3."
        
        result = ""

        for i in range(n):
              result += " " * i
              result += "*" * (2 * (n - 1) - 1)
              if i < n -1:
                result += "/n"

        return result

   
    

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()
