def solve(v):
    d[v][0] = 0
    d[v][1] = weights[v]

    for i in tree[v]:
        solve(i)

    for i in tree[v]:
        d[v][1] += d[i][0]
        d[v][0] += max(d[i][0], d[i][1])


with open("selectw.in") as f:
    n = int(f.readline())
    tree = [[] for _ in range(n)]
    weights = [0 for _ in range(n)]
    root = 0
    for i in range(n):
        tmp, weight = map(int, f.readline().split())
        weights[i] = weight
        if tmp == 0:
            root = i
        else:
            tree[tmp - 1].append(i)

d = [[0, 0] for _ in range(n)]
solve(root)
with open("selectw.out", "w") as f:
    f.write(str(max(d[root][0], d[root][1])))
