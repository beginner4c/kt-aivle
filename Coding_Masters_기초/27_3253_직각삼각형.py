a = input().split()
a = list(map(int, a))
a = sorted(a, reverse=False)
print(a[0] * a[1] // 2)
