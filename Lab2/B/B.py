from sys import setrecursionlimit
import threading

threading.stack_size(8 * 1024 * 1024 * 16)
setrecursionlimit(10 ** 9)


def main():
    def dfs(vertex):
        nonlocal cycle_start
        graph[vertex][0] = 1
        path.append(vertex + 1)
        for i in range(1, len(graph[vertex])):
            next_vertex = graph[vertex][i]
            if graph[next_vertex][0] == 0:
                if dfs(graph[vertex][i]):
                    stack.append(vertex + 1)
                    return True
            elif graph[next_vertex][0] == 1:
                stack.append(vertex + 1)
                cycle_start = next_vertex + 1
                return True
        graph[vertex][0] = 2
        path.pop()

    with open("cycle.in") as f:
        n, m = list(map(int, f.readline().split()))
        graph = [[0] for _ in range(n)]
        cycle_start = None

        for i in range(m):
            a, b = list(map(int, f.readline().split()))
            graph[a - 1].append(b - 1)

    path = []
    stack = []
    final = []

    with open("cycle.out", "w") as f:
        for i in range(len(graph)):
            if graph[i][0] == 0:
                if dfs(i):
                    f.write("YES\n")
                    for elem in stack:
                        if elem != cycle_start:
                            final.append(elem)
                        else:
                            final.append(elem)
                            break
                    for i in range(path.index(cycle_start), len(path)):
                        f.write(str(path[i]) + " ")
                    break
        else:
            f.write("NO")


threading.Thread(target=main).start()
