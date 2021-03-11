from sys import setrecursionlimit
import threading

threading.stack_size(8 * 1024 * 1024 * 16)
setrecursionlimit(10 ** 9)


def main():
    def dfs_top(vertex):
        visited[vertex] = 1
        for i in range(len(graph[vertex])):
            next_vertex = graph[vertex][i]
            if visited[next_vertex] == 0:
                dfs_top(next_vertex)
        top.append(vertex)

    def dfs_col(vertex, index):
        color[vertex] = index
        for i in range(len(graph_r[vertex])):
            go_to = graph_r[vertex][i]
            if color[go_to] == 0:
                dfs_col(go_to, index)

    with open("cond.in") as f:
        n, m = list(map(int, f.readline().split()))
        graph = [[] for _ in range(n)]
        graph_r = [[] for _ in range(n)]

        for i in range(m):
            a, b = list(map(int, f.readline().split()))
            graph[a - 1].append(b - 1)
            graph_r[b - 1].append(a - 1)

    top = []
    visited = [0 for _ in range(n)]
    color = [0 for _ in range(n)]
    component = 1

    for i in range(n):
        if visited[i] == 0:
            dfs_top(i)

    for i in range(1, n + 1):
        if color[top[n - i]] == 0:
            dfs_col(top[n - i], component)
            component += 1

    with open("cond.out", "w") as f:
        f.write(str(component - 1) + "\n")
        for i in range(n):
            f.write(str(color[i]) + " ")


threading.Thread(target=main).start()
