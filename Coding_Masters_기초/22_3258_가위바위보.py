N = int(input())
mink = 0
dong = 0

for i in range(N) :
    check = input().split()
    res0, res1 = int(check[0]), int(check[1])

    if (res0 == 1 and res1 == 3):
        mink += 1
    elif (res0 == 2 and res1 == 1) :
        mink += 1
    elif (res0 == 3 and res1 == 2) :
        mink += 1
    elif (res1 == 1 and res0 == 3) :
        dong += 1
    elif (res1 == 2 and res0 == 1) :
        dong += 1
    elif (res1 == 3 and res0 == 2) :
        dong += 1

print(mink, dong)
