def bfs(graph, track, used, distance, way, finish, m):
    while len(track) != 0:
        curVert = track[0]
        del track[0]

        for j in range(len(graph[curVert])):
            if used[graph[curVert][j]] == 0:
                if (graph[curVert][j] == curVert + 1) and (m != 1):
                    way[graph[curVert][j]] = way[curVert] + 'R'
                elif (graph[curVert][j] == curVert - 1) and (m != 1):
                    way[graph[curVert][j]] = way[curVert] + 'L'
                elif graph[curVert][j] == curVert + m:
                    way[graph[curVert][j]] = way[curVert] + 'D'
                elif graph[curVert][j] == curVert - m:
                    way[graph[curVert][j]] = way[curVert] + 'U'

                track.append(graph[curVert][j])
                used[graph[curVert][j]] += 1
                distance[graph[curVert][j]] = distance[curVert] + 1
                if graph[curVert][j] == finish:
                    return distance[graph[curVert][j]]
    return 0


labyrinth = []
with open("input.txt") as f:
    n, m = map(int, f.readline().split())
    i = 0
    for line in f.readlines():
        if line[-1] == "\n":
            line = line[:-1]
        for symbol in line:
            if symbol == "S":
                start = i
            elif symbol == "T":
                finish = i
            labyrinth.append(symbol)
            i += 1

graph = [[] for _ in range(len(labyrinth))]
for i in range(len(labyrinth)):
    if (labyrinth[i] == '.') or (labyrinth[i] == 'S') or (labyrinth[i] == 'T'):
        if (i - 1 > -1) and (i % m != 0) and (
                (labyrinth[i - 1] == '.') or (labyrinth[i - 1] == 'S') or (labyrinth[i - 1] == 'T')):
            graph[i].append(i - 1)

        if (i + 1 < n * m) and ((i + 1) % m != 0) and (
                (labyrinth[i + 1] == '.') or (labyrinth[i + 1] == 'S') or (labyrinth[i + 1] == 'T')):
            graph[i].append(i + 1)

        if (i + m < n * m) and ((labyrinth[i + m] == '.') or (labyrinth[i + m] == 'S') or (labyrinth[i + m] == 'T')):
            graph[i].append(i + m)

        if (i - m > -1) and ((labyrinth[i - m] == '.') or (labyrinth[i - m] == 'S') or (labyrinth[i - m] == 'T')):
            graph[i].append(i - m)

distance = [0 for _ in range(n * m)]
used = [0 for _ in range(n * m)]
used[start] = 1
track = [start]
way = ["" for _ in range(len(graph))]

distanceFinish = bfs(graph, track, used, distance, way, finish, m)

with open("output.txt", "w") as f:
    if distanceFinish == 0:
        f.write("-1")
    else:
        f.write(str(distanceFinish) + "\n")
        f.write(way[finish])
