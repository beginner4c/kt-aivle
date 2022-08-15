a = input().split()
a = list(map(int, a)) # 리스트 정수로 변환

print(sum(a) // len(a))
