A = input().split()
A = list(map(int, A))

if 4 >= A[1] / A[0] * 100:
    print("YES")
else :
    print("NO")
