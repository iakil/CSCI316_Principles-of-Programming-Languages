from typing import List

a: List = []
N: int = 3
# a = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    a.append([])
    for j in range(N):
        a[i].append(0)
print(a)
