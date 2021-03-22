from sys import setrecursionlimit
import threading

threading.stack_size(8 * 1024 * 1024 * 16)
setrecursionlimit(10 ** 9)


def main():
    def countWeight(a, b):
        return ((graph[b][0] - graph[a][0]) * (graph[b][0] - graph[a][0]) +
                (graph[b][1] - graph[a][1]) * (graph[b][1] - graph[a][1])) ** 0.5

    with open("spantree.in") as f:
        n = int(f.readline())
        graph = [[0, 0] for _ in range(n)]
        for i in range(n):
            graph[i][0], graph[i][1] = map(int, f.readline().split())

    answer = 0
    distance = [10 ** 9 for _ in range(n)]
    visited = [False for _ in range(n)]
    path = [-1 for _ in range(n)]

    distance[0] = 0
    for i in range(n):
        v = -1
        for j in range(n):
            if not visited[j] and (v == -1 or distance[j] < distance[v]):
                v = j
        visited[v] = True

        if path[v] != -1:
            answer += countWeight(v, path[v])

        for next in range(n):
            temp = countWeight(v, next)
            if temp < distance[next]:
                distance[next] = temp
                path[next] = v

    with open("spantree.out", "w") as f:
        f.write(str(answer))


threading.Thread(target=main).start()
