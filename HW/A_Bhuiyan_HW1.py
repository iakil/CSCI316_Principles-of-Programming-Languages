# Akil Bhuiyan
# Professor Joshua Waxman
# CSCI 316
# HW1 - Find the area of a circle in Python

def compute_area_circle():
  # Akil Bhuiyan
    
    def foo():
        print("\nAkil Bhuiyan\nProfessor Joshua Waxman\nCSCI 316\nHW1\n")


    def getRadius() -> None:
          nonlocal radius
          radius = int (input("Enter the radius of the circle:\t"))
   
    def ProcessArea() -> None:
        nonlocal area
        area = PI * radius ** 2

    def printArea() -> None:
        print (f"\nArea of the circle is: {area}")
  

    # make definitions here
    radius:int = 0
    PI:float = 3.14 # value of PI
    area:float = 0.0


    foo()

    # get the radius using a function
    getRadius()

    # processing using a function
    ProcessArea()

    # output the area here by calling a function
    printArea()
    
compute_area_circle()

