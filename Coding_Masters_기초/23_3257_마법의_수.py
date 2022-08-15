N = int(input())
check = N * 3

for i in range(N, N * 3):
    if i % N == 0 and i % 3 == 0 :
        check = i
        break
print(check)
