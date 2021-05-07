with open("prefix.in") as f:
    string = f.readline()[:-1]

p = [0 for _ in range(len(string))]
for i in range(1, len(string)):
    k = p[i - 1]
    while k > 0 and string[i] != string[k]:
        k = p[k - 1]
    if string[i] == string[k]:
        k += 1
    p[i] = k

with open("prefix.out", "w") as f:
    f.write(' '.join(str(i) for i in p))
