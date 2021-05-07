def z_function(string):
    n = len(string)
    z_f = [0 for _ in range(n)]
    left, right = 0, 0
    for i in range(1, n):
        z_f[i] = max(0, min(right - i, z_f[i - left]))
        while i + z_f[i] < n and string[z_f[i]] == string[i + z_f[i]]:
            z_f[i] += 1
        if i + z_f[i] > right:
            left = i
            right = i + z_f[i]
    return z_f



def substring_search(text, pattern):
    n, m = len(text), len(pattern)
    answer = []
    z_f = z_function(pattern + '#' + text)
    for i in range(m + 1 , n + 2):
        if z_f[i] == m:
            answer.append(i - m)
    return answer


with open("search2.in") as f:
    p = f.readline()[:-1]
    t = f.readline()

ans = substring_search(t, p)

with open("search2.out", "w") as f:
    f.write(str(len(ans)) + '\n')
    for a in ans:
        f.write(str(a) + " ")