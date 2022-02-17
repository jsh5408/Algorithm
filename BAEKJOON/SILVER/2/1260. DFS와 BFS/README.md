## 1260. DFS와 BFS - python3
https://www.acmicpc.net/problem/1260

#### 내 풀이 - 실패
```
N, M, V = map(int, input().split())

graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph.keys():
    graph[g].sort()

b = []
d = []

### DFS
visited = {i:0 for i in range(1, N+1)}
def dfs(graph, v):
    visited[v] = 1
    d.append(v)

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i)
    
dfs(graph, V)
print(d)

### BFS
visited = {i:0 for i in range(1, N+1)}
queue = [V]
while queue:
    q = queue.pop(0)
    visited[q] = 1
    b.append(q)
    for i in graph[q]:
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)

print(b)
```
graph 를 만들어서 각 정점마다 연결된 노드들을 저장
작은 숫자부터 가야한다고 했으므로 sort()

dfs 는 visited 와 재귀 함수를 이용해서 탐색
bfs 는 visited 와 queue 를 이용해서 탐색

한 11퍼 통과하다 실패했다...

참고) 1 ~ N 까지의 숫자이므로 굳이 딕셔너리 사용할 필요 X -> 리스트 사용

#### 내 풀이 2 - 성공
```
N, M, V = map(int, input().split())

graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph.keys():
    graph[g].sort()

b = []
d = []

### DFS
visited = {i:0 for i in range(1, N+1)}
def dfs(graph, v):
    print(v, end=' ')
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i)
    
dfs(graph, V)
print()

### BFS
visited = {i:0 for i in range(1, N+1)}
queue = [V]
while queue:
    q = queue.pop(0)
    visited[q] = 1
    print(q, end= ' ')
    for i in graph[q]:
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)
```
dfs, bfs 모두 탐색하는 과정에서
결과값을 변수에 저장하지 않고 바로 print 를 해주니까 통과 됐다

`print(q, end= ' ')` => 다음 값이 공백을 사이에 두고 같은 줄에 출력 (엔터 X)

> 처음엔 바보같이 **리스트를 그대로 출력**해서 절대 통과 안된 것이었음...
```
for i in d:
    print(i, end=" ")
print()
for i in b:
    print(i, end=" ")
```
를 해주면 통과 된다...^^
>
> 주의 하자!!!

![](https://images.velog.io/images/jsh5408/post/f3e2d936-e40d-42b4-b386-64202247521e/image.png)