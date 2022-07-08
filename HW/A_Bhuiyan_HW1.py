# Akil Bhuiyan
# Professor Joshua Waxman
# CSCI 316
# HW1

PI:float = 3.141592653589793 # value of PI

def compute_area_circle():
  # Akil Bhuiyan
    
    def foo():
        print("Akil Bhuiyan\nProfessor Joshua Waxman\nCSCI 316\nHW1\n")
  
  # make definitions here
    radius:int = 0
    area:float = PI * radius ** 2
  
  # get the radius using a function
    
    def getRadius():
        nonlocal radius
        radius = int (input("Enter the radius of the circle:\t"))

  # get the area using a function

    def getArea():
        nonlocal area
        area = PI * radius ** 2

  # print the area using a function

    def printArea():
        print (f"\nArea of the circle is: {area}")
  
  # processing using a function
    foo()
    getRadius()
    getArea()
  # output the area here by calling a function
    printArea()
    
compute_area_circle()