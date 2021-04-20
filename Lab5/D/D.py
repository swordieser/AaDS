with open("knight2.in") as f:
    n, m = map(int, f.readline().split())

chessboard = [[0 for _ in range(m)] for _ in range(n)]
chessboard[0][0] = 1


def solve(i, j):
    if 0 <= i < n and 0 <= j < m:
        if chessboard[i][j] == 0:
            chessboard[i][j] = solve(i - 2, j - 1) + solve(i - 2, j + 1) + solve(i - 1, j - 2) + solve(i + 1, j - 2)
    else:
        return 0
    return chessboard[i][j]


with open("knight2.out", "w") as f:
    f.write(str(solve(n-1, m-1)))
