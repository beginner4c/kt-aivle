NM = input().split()
row, col = int(NM[0]), int(NM[1])
_color = {"R" : 12, "G" : 23, "B" : 34, 35 : "Y", 57 : "C", 46 : "M"}

A = [[0]*col for i in range(row)]
for i in range(row) :
    A[i] = input().split()

B = [[0]*col for i in range(row)]
for i in range(row) :
    B[i] = input().split()

C = [[0]*col for i in range(row)]


for i in range(row) :
    for j in range(col) :
        if A[i][j] == B[i][j] :
            C[i][j] = A[i][j]
        else :
            ind = _color[A[i][j]] + _color[B[i][j]]
            C[i][j] = _color[ind]

for i in range(row) :
    for j in range(col) :
        print(C[i][j], end=" ")
    print()
