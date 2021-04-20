def solve(v):
    d[v][0] = 0
    d[v][1] = 1

    for i in tree[v]:
        solve(i)

    for i in tree[v]:
        d[v][1] += d[i][0]
        d[v][0] += max(d[i][0], d[i][1])


n = int(input())
tree = [[] for _ in range(n)]

root = 0
for i in range(n):
    tmp = int(input())
    if tmp == 0:
        root = i
    else:
        tree[tmp-1].append(i)

d = [[0, 0] for _ in range(n)]
solve(root)
print(max(d[root][0], d[root][1]))
