from sys import setrecursionlimit
import threading

threading.stack_size(8 * 1024 * 1024 * 16)
setrecursionlimit(10 ** 9)


def main():
    def dfs(vertex):
        visited[vertex] = 1
        for i in range(len(graph[vertex])):
            next_vertex = graph[vertex][i]
            if not visited[next_vertex]:
                dfs(next_vertex)
        top.append(vertex)

    with open("hamiltonian.in") as f:
        n, m = list(map(int, f.readline().split()))
        graph = [[] for _ in range(n)]
        for i in range(m):
            a, b = list(map(int, f.readline().split()))
            graph[a - 1].append(b - 1)

    visited = [0 for _ in range(n)]
    exist = False
    top = []
    ans = "YES"

    for i in range(n):
        if visited[i] == 0:
            dfs(i)

    for i in range(len(top) - 1, 0, -1):
        for j in graph[top[i]]:
            if top[i - 1] == j:
                ans = "YES"
                exist = True
                break
        if not exist:
            ans = "NO"
            break
        exist = False

    with open("hamiltonian.out", "w") as f:
        f.write(ans)


threading.Thread(target=main).start()
