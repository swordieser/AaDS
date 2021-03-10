from sys import setrecursionlimit
import threading

threading.stack_size(8*1024*1024*16)
setrecursionlimit(10 ** 9)


def main():
    def dfs(vertex):
        graph[vertex][0] = 1
        for i in range(1, len(graph[vertex])):
            next_vertex = graph[vertex][i]
            if graph[next_vertex][0] == 0:
                if dfs(graph[vertex][i]):
                    return True
            elif graph[next_vertex][0] == 1:
                return True
        graph[vertex][0] = 2
        answer.append(vertex + 1)

    with open("topsort.in") as f:
        n, m = list(map(int, f.readline().split()))
        graph = [[0] for _ in range(n)]
        for i in range(m):
            a, b = list(map(int, f.readline().split()))
            graph[a - 1].append(b - 1)

    answer = []

    with open("topsort.out", "w") as f:
        for i in range(len(graph)):
            if graph[i][0] == 0:
                if dfs(i):
                    f.write("-1")
                    break
        else:
            for i in range(len(answer)):
                f.write(str(answer.pop()) + " ")


threading.Thread(target=main).start()
