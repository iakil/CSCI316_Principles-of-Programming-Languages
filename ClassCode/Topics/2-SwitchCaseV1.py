# Use switch statement in Python 
# v1

x: int = 0
y: int = 0
x  = int(input ("Please enter a number"))

if x == 1: 
  print ("Hello Akil!")
  y = 9
elif x == 2:
  print ("Goodbye Akil")
  y = 0
else:
  print ("Invalid Choice")

print ("The value of y is " + str(y)) # convert is to string cz concatenation alllowed only string to string
# or 
print ("The value of y is " , y)