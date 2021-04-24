with open("search1.in") as f:
    p = f.readline()[:-1]
    t = f.readline()

answer = []
n, m = len(t), len(p)
for i in range(n - m + 1):
    if t[i:i + m] == p:
        answer.append(i)

with open("search1.out", "w") as f:
    f.write(str(len(answer)) + '\n')
    for a in answer:
        f.write(str(a + 1) + " ")
