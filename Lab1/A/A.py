with open("input.txt") as f:
    n, m = map(int, f.readline().split())
    ans = [["0" for _ in range(n)] for _ in range(n)]
    for i in range(m):
        a, b = map(int, f.readline().split())
        ans[a-1][b-1] = "1"

with open("output.txt", "w") as f:
    for a in ans:
        for b in a:
            f.write(b + " ")
        f.write("\n")
