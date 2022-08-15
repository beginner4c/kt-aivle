ip = input()
check_ip = list(ip)
check = 0

for i in range(0, len(check_ip)) :
    if check_ip[i] == '.' :
        check += 1
        break

if check != 0 :
    for i in range(check) :
        print("IPv4")
else :
    print("IPv6")
