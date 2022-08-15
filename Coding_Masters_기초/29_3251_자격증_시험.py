P = input().split()
P = list(map(int, P))
check = 0

for i in range(len(P)):
    if P[i] < 40 :
        check += 1
        break

if check == 0 and sum(P) // len(P) >= 60:
    print("P")
else :
    print("F")
