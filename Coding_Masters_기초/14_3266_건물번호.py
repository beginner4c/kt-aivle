"""
T = int(input())
t = T % 2
N = []
res = []

for i in range(T) :
    N.append(int(input()))
    if N[i] % 2 == t :
        res.append("L")
    else :
        res.append("R")

for i in range(T) :
    print(res[i])
"""

T = int(input())
result = []

for i in range(T) :
    N = int(input())
    if N % 2 == 1 :
        result.append("L")
    else :
        result.append("R")

for i in range(T) :
    print(result[i])
