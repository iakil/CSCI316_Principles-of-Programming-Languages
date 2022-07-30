# Switch Case in Python
# v2

from typing import Dict, Callable
def main():
  x: int = 0
  y: int = 0
  x = int (input("Please enter a number"))

# We can use nonlocal variable only in nested function
# nonlocal refer to the same variable within nested fuction

  def one(): nonlocal y; print ("Hello Akil!"); y=9 # we can write this code in one line using semicolon
  def two(): nonlocal y; print ("Goodbye Akil"); y=18
  def default():  print ("Invalid Choice")

  d: Dict[int, Callable] = {1: one, 2: two}
  if x in d:
    d[x]()
  else:
    default()

  print ("The value of y is " , y)

main()