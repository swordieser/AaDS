parallel = False
with open("input.txt") as f:
    n, m = map(int, f.readline().split())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        a, b = map(int, f.readline().split())
        a -= 1
        b -= 1
        if a != b:
            matrix[a][b] += 1
            matrix[b][a] += 1
        else:
            matrix[a][b] += 1
        if matrix[a][b] > 1:
            parallel = True
            break


with open("output.txt", "w") as f:
    if parallel:
        f.write("YES")
    else:
        f.write("NO")
