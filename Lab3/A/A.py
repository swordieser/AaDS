from sys import setrecursionlimit
import threading

threading.stack_size(8 * 1024 * 1024 * 16)
setrecursionlimit(10 ** 9)


def main():
    with open("input.txt") as f:
        n, m = list(map(int, f.readline().split()))
        graph = [0 for _ in range(n)]
        for i in range(m):
            a, b = list(map(int, f.readline().split()))
            graph[a - 1] += 1
            graph[b - 1] += 1

    with open("output.txt", "w") as f:
        for v in graph:
            f.write(str(v) + " ")


threading.Thread(target=main).start()
