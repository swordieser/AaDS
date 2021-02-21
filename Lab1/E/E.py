def bfs(start):
    color = ["white"] * n
    distance = [n+1] * n
    parent = [-1] * n

    color[start] = "gray"
    distance[start] = 0
    q = [start]
    while len(q) != 0:
        u = q[0]
        q.remove(u)
        for v in matrix[u]:
            if color[v] == "white" and distance[u] + 1 < distance[v]:
                color[v] = "gray"
                distance[v] = distance[u] + 1
                parent[v] = u
                q.append(v)
        color[u] = "black"

    return distance


with open("pathbge1.in") as f:
    n, m = map(int, f.readline().split())
    matrix = [[] for _ in range(n)]
    for i in range(m):
        b, e = map(int, f.readline().split())
        b -= 1
        e -= 1
        matrix[b].append(e)
        matrix[e].append(b)

d = bfs(0)

with open("pathbge1.out", "w") as f:
    f.write(" ".join(map(str, d)))
