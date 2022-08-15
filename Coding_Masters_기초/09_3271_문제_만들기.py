N = int(input())
a = input().split()
check = 100

for i in range(N) :
    check -= int(a[i])

if check < 0 :
    check = 0

print(check)
