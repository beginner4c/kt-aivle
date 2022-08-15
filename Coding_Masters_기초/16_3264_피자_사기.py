from math import pi

def cir(hal) :
    return hal * hal * pi

Piz = input().split()
Piz = list(map(int, Piz))

if cir(Piz[0]) > cir(Piz[1]) * Piz[2] :
    print("NO")
else :
    print("YES")
