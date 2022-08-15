check = int(input())
if check % 2 == 0 :
    check += 2
else :
    check += 1

while True :
    if (check // 2) % 2 == 1:
        print(check)
        break
    check += 2
