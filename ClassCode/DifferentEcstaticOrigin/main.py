# def factorial(n: int) -> int:
#   prod = 1
#   for i in range(1, n+1):
#     prod *= i
#   return prod

# def main():
#   print(factorial(5))  

# main()

# x: int = 0
# y: int = 0
# x = int(input("Please enter a number"))

# if x == 1:
#   print("hello")
#   y = 3
# elif x == 2:
#   print("goodbye")
#   y = 0
# else:
#   print("invalid choice")

# print("The value of y is", y)

# from typing import Dict, Callable

# def main():
#   x: int = 0
#   y: int = 0
#   x = int(input("Please enter a number"))

#   def one(): nonlocal y; print("hello"); y = 3
#   def two(): nonlocal y; print("goodbye"); y = 9
#   def default(): print("invalid choice")

#   d: Dict[int, Callable] = {1: one, 2: two}
#   if x in d:
#     d[x]()
#   else:
#     default()

#   print("The value of y is", y)

# main()

# from typing import Set

# s = set()
# s.add(1)
# s.add(1)
# s.add(1)
# s.add(2)
# print(s)
# print(1 in s)

# x = int(input("please enter a number: "))
# y = int(input("please enter another number: "))
# z = x + y
# print(z)

# import csv
# f = open("myfile.csv", "r")
# reader = csv.reader(f)
# for line in reader:
#   a, b, c = line
#   print(a)
#   fv = a + b
# f.close()

radius = input()
PI = 0 # make this the right value
area = PI * radius ** 2
print(area)

def compute_area_circle():
  # put your name in a comment here
  
  # make definitions here
  radius:int = 0
  
  # get the radius using a function
  
  # processing using a function

  # output the area here by calling a function
  
  pass

compute_area_circle()