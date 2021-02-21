def dfs(index, num):
    visited[index] = num
    for i in range(n):
        if matrix[index][i] == 1 and not visited[i]:
            dfs(i, num)


with open("components.in") as f:
    n, m = map(int, f.readline().split())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        b, e = map(int, f.readline().split())
        b -= 1
        e -= 1
        matrix[b][e] = matrix[e][b] = 1

visited = [0 for _ in range(n)]
quantity = 0
number = 0
for i in range(n):
    if not visited[i]:
        quantity += 1
        number += 1
        dfs(i, number)

with open("components.out", "w") as f:
    f.write(str(quantity) + '\n')
    f.write(" ".join(map(str, visited)))
