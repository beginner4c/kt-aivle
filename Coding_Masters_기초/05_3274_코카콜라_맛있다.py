num = int(input())
menu = ["empty","jjamppong","jjajangmyeon","bokkeumbap","jjajangmyeon"]
count = 0

for i in range(num) :
    count += 1
    if count == 5 :
        count = 1

print(menu[count])
