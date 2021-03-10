from sys import setrecursionlimit
import threading

threading.stack_size(8 * 1024 * 1024 * 16)
setrecursionlimit(10 ** 9)


def main():
    def dfs(vertex):
        nonlocal cycle, path
        path.append(vertex)
        color[vertex] = 1
        for u in graph[vertex]:
            if color[u] == 0:
                dfs(u)
            if color[u] == 1:
                cycle = True
        color[vertex] = 2

    with open("cycle.in") as f:
        n, m = list(map(int, f.readline().split()))
        graph = [[] for _ in range(n)]
        for i in range(m):
            a, b = list(map(int, f.readline().split()))
            graph[a - 1].append(b - 1)

    color = [0 for _ in range(n)]  # 0 - white, 1 - grey, 2 - black
    cycle = False
    path = []
    for i in range(n):
        if color[i] == 0:
            path = []
            dfs(i)
            if cycle:
                break

    path.append(path[0])
    del path[0]

    with open("cycle.out", "w") as f:
        if cycle:
            f.write("YES\n")
            for v in path:
                f.write(str(v+1) + " ")

        else:
            f.write("NO")


threading.Thread(target=main).start()
