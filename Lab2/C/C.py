from sys import setrecursionlimit
import threading

threading.stack_size(8 * 1024 * 1024 * 16)
setrecursionlimit(10 ** 9)


def main():
    def dfs(vertex, color):
        nonlocal bipartite
        graph[vertex][0] = color
        for i in range(1, len(graph[vertex])):
            next_vertex = graph[vertex][i]
            if graph[next_vertex][0] is None:
                if dfs(next_vertex, not color):
                    return True
            elif graph[next_vertex][0] == color:
                bipartite = False
                return True

    with open("bipartite.in") as f:
        n, m = list(map(int, f.readline().split()))
        graph = [[None] for _ in range(n)]
        for i in range(m):
            a, b = list(map(int, f.readline().split()))
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)

    bipartite = True
    for i in range(len(graph)):
        if graph[i][0] is None:
            if dfs(i, True):
                break
    ans = "YES" if bipartite else "NO"

    with open("bipartite.out", "w") as f:
        f.write(ans)


threading.Thread(target=main).start()
