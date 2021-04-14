n = int(input())
sequence = list(map(int, input().split()))

prev = [0 for _ in range(n)]
d = [0 for _ in range(n)]

for i in range(n):
    d[i] = 1
    prev[i] = -1
    for j in range(i):
        if (sequence[j] < sequence[i]) and (d[j] + 1 > d[i]):
            d[i] = d[j] + 1
            prev[i] = j

pos = 0
length = d[0]
for i in range(n):
    if d[i] > length:
        pos = i
        length = d[i]

answer = []
while pos != -1:
    answer.append(sequence[pos])
    pos = prev[pos]

answer.reverse()

print(len(answer))
print(*answer)
