def DFS(index, number):
    visited[index] = number
    for i in range(n):
        if matrix[index][i] == 1 and not visited[i]:
            DFS(i, number)


with open("components.in") as f:
    n, m = map(int, f.readline().split())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        b, e = map(int, f.readline().split())
        b -= 1
        e -= 1
        matrix[b][e] = matrix[e][b] = 1

visited = [0 for _ in range(n)]

number = 0
for i in range(n):
    if not visited[i]:
        number += 1
        DFS(i, number)
