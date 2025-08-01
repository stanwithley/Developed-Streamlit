satr, soton = map(int, input().split())

matrix = []
for _ in range(satr):
    khat = list(map(int, input().split()))
    matrix.append(khat)

x = int(input())
x = x % 4

for _ in range(x):
    matrix_jadid = []
    for j in range(len(matrix[0])):
        khat_jadid = []
        for i in range(len(matrix) -1, -1, -1):
            khat_jadid.append(matrix[i][j])
        matrix_jadid.append(khat_jadid)
    matrix = matrix_jadid

for khat in matrix:
    for adad in khat:
        print(adad, end=' ')
    print()
