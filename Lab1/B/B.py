with open("input.txt") as f:
    n = int(f.readline())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, f.readline().split())))

isAdjacencyMatrix = True
j = 0
for i in range(n):
    if matrix[i][i] == 1:
        isAdjacencyMatrix = False
        break
    else:
        for k in range(j, n):
            if matrix[i][k] != matrix[k][i]:
                isAdjacencyMatrix = False
                break
        j += 1
with open("output.txt", "w") as f:
    if isAdjacencyMatrix:
        f.write("YES")
    else:
        f.write("NO")
