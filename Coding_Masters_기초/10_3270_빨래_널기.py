a = input().split() # 빨래
x = input().split() # 옷걸이
temp = 0
check = int(x[0]) - int(a[0])

if int(x[1]) < int(a[1]):
    temp = int(a[1]) - int(x[1])

if check < 0 or check - temp < 0:
    print("NO")
else :
    print("YES")
