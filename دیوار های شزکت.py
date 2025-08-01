n = int(input())
grid = [[0] * 101 for _ in range(101)]

for row in range(n):
    l, r = map(int, input().split())
    for col in range(l, r):
        grid[row][col] = 1

perimeter = 0
for i in range(n):
    for j in range(101):
        if grid[i][j] == 1:
            if i == 0 or grid[i-1][j] == 0:
                perimeter += 1
            if i == n-1 or grid[i+1][j] == 0:
                perimeter += 1
            if j == 0 or grid[i][j-1] == 0:
                perimeter += 1
            if j == 100 or grid[i][j+1] == 0:
                perimeter += 1

print(perimeter)
