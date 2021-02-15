def dfs(n):
    used[n] = 1
    for i in range(len(mas[n])):
        if used[mas[n][i]] == 0:
            print(mas[n][i])
            dfs(mas[n][i])

n, m = map(int, input().split())
mas = []
for i in range(n):
    mas.append([])
    for j in range(n):
        if j!=i:
            mas[-1].append(j)
print(mas)
for i in range(m):
    s, e = map(int, input().split())
    idx1 = mas[s-1].index(e-1)
    idx2 = mas[e-1].index(s-1)
    mas[s-1].pop(idx1)
    mas[e-1].pop(idx2)
print(mas)
used = [0]*n
dfs(1)
