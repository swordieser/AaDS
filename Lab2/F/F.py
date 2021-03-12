from sys import setrecursionlimit
import threading

threading.stack_size(8 * 1024 * 1024 * 16)
setrecursionlimit(10 ** 9)


def main():
    def search(start_vertex):
        stack = [start_vertex]
        while len(stack) != 0:
            next_vertex = stack[-1]
            if visited[next_vertex] == 1:
                winner_vertex = 0
                for i in graph[next_vertex]:
                    if winner[i] == 0:
                        winner_vertex = 1
                winner[next_vertex] = winner_vertex
                visited[next_vertex] = 2
                del stack[-1]
                continue
            elif visited[next_vertex] == 2:
                del stack[-1]
                continue
            visited[next_vertex] = 1
            for i in graph[next_vertex]:
                if visited[i] == 0:
                    stack.append(i)

    with open("game.in") as f:
        n, m, start = list(map(int, f.readline().split()))
        graph = [[] for _ in range(n)]
        for i in range(m):
            a, b = list(map(int, f.readline().split()))
            graph[a - 1].append(b - 1)

    visited = [0 for _ in range(n)]  # 0 - white, 1 - grey, 2 - black
    winner = [0 for _ in range(n)]
    search(start - 1)
    ans = "First player wins" if winner[start - 1] == 1 else "Second player wins"

    with open("game.out", "w") as f:
        f.write(ans)


threading.Thread(target=main).start()
