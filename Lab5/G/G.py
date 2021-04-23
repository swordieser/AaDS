with open("knapsack.in") as f:
    s, n = map(int, f.readline().split())
    weights = list(map(int, f.readline().split()))

backpack = [0 for _ in range(100000)]
backpack[0] = 1

for w in weights:
    for i in range(s, w - 1, -1):
        if backpack[i - w] == 1:
            backpack[i] = 1

with open("knapsack.out", "w") as f:
    for i in range(s, 0, -1):
        if backpack[i] == 1:
            f.write(str(i))
            break
