check = input()
check = check.split()
price = [1000, 1500, 2000, 3000, 5000]
pay = 0

for i in range(0, len(check)):
    pay += int(check[i]) * price[i]

print(pay)
