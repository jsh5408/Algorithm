N, M = map(int, input().split())

graph = {i:[] for i in range(1, N+1)}
person = {i:[0]*(N+1) for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    person[a][b] = 1
    person[b][a] = 1

def func(p, target, cnt, visited):
    if person[p][target] > 0:
        return cnt + person[p][target]

    if p == target:
        return cnt
    
    ans = N
    for i in graph[p]:
        if i not in visited:
            ans = min(ans, func(i, target, cnt+1, visited+[p]))
    return ans

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if person[i][j] == 0:
            cnt = func(i, j, 0, [])
            person[i][j] = cnt
            person[j][i] = cnt


sums = []
for i in range(1, N+1):
    sums.append(sum(person[i]))
    
m = min(sums)
for i in range(len(sums)):
    if m == sums[i]:
        print(i+1)
        break