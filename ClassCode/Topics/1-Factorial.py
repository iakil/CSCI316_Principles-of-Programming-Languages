# Approaches the coding by exploring how other programming language do it
def factorial (n: int) -> int:  # datatype of n is int and return type of the func factorial is also int
  factResult = 1
  for i in range (1,n+1):
    factResult *= i
  return factResult
def main(): # initialize our program with main function
  print(factorial(10))  
main()