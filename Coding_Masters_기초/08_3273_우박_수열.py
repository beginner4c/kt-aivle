num = int(input())

while num != 1 :
    print(num, end=" ")
    if num % 2 == 0 : # 짝수인 경우
        num = num // 2
    else : # 홀수인 경우
        num = 3 * num + 1

print(num)
