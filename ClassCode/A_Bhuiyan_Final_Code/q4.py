from typing import List
a: List = []
N: int = 3
a = [1,2,3,4]

def foo(b: List):
    b.append(5)
    b = b + [6]

foo(a)
print(a)