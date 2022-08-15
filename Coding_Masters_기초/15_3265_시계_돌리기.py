A = input().split()
A = list(map(int, A))
B = []
B.append(max(A) - min(A))
B.append(60 + min(A) - max(A))

print(min(B))
