def printLCS(i, j):
    if i == 0 or j == 0:
        return
    if prev[i][j] == [i - 1, j - 1]:
        printLCS(i - 1, j - 1)
        print(first[i])
    else:
        if prev[i][j] == [i - 1, j]:
            printLCS(i - 1, j)
        else:
            printLCS(i, j - 1)


first = input()
second = input()

m = len(first)
n = len(second)
lcs = [[0 for _ in range(n)] for _ in range(m)]
prev = [[[] for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m):
    for j in range(1, n):
        if first[i] == second[j]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
            prev[i][j] = [i - 1, j - 1]
        else:
            if lcs[i - 1][j] >= lcs[i][j - 1]:
                lcs[i][j] = lcs[i - 1][j]
                prev[i][j] = [i - 1, j]
            else:
                lcs[i][j] = lcs[i][j - 1]
                prev[i][j] = [i, j - 1]


printLCS(m, n)
