num = input()
num2 = list(num)
check = 0

for i in range(0, len(num2)) :
    if num2[i] == '3' or num2[i] == '6' or num2[i] == '9' :
        check += 1

if check != 0 :
    for i in range(check) :
        print("clap",end="")
else :
    print(num)
