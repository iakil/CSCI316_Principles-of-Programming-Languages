# common error in python using type checking
# specially in back python programmer get errors for types
import csv
f = open("myfile.csv", "r")
reader = csv.reader(f)

for line in reader:
    a, b, c = line
    print(a)
    fv = a + b
f.close()
