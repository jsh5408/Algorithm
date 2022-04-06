## 가장 먼 노드
https://programmers.co.kr/learn/courses/30/lessons/49189

#### 내 풀이 - 실패
```
answer = 0
maxlen = 0
dp = []

def func(dic, n, cnt, path):
    global answer, maxlen, dp
    
    if dp[n] < cnt:
        return
    
    dp[n] = min(dp[n], cnt)
    
    for i in range(len(dic[n])):
        a = dic[n][i]
        if a not in path:
            path.add(a)
            func(dic, a, dp[n]+1, path)
            path.remove(a)

def solution(n, edge):
    global answer, dp
    dic = {i:[] for i in range(1, n+1)}
    dp = [float('inf')] * (n+1)
    
    for a, b in edge:
        dic[a].append(b)
        dic[b].append(a)
    
    func(dic, 1, 0, {1})
    
    m = 0
    for d in dp:
        if d != float('inf') and m < d:
            m = d
    answer = dp.count(m)
    
    return answer
```
`dic` 에 `1 ~ n` 까지의 노드들과 각 노드마다 연결 현황 저장
`n` 길이의 `dp` 도 만들어줌

재귀함수 돌려서 각 노드마다 최단 경로를 `dp` 에 update

`cnt` : 경로의 길이

최단 경로면 굳이 왔던 곳을 다시 올 필요는 없을 것 같아서
`path` 를 이용해서 지나간 노드들을 모두 저장

다음 재귀로 넘어갈때는 처음 보는 노드로만 이동

`dp` 의 최댓값을 찾아서 개수 return

![](https://images.velog.io/images/jsh5408/post/4ecf4f69-cb50-45fc-a762-86be0feb515d/image.png)

#### 다른 사람의 풀이
```
def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    m = max(distances)
    answer = distances.count(m)

    return answer
```
재귀 말고 `queue` 를 이용한 bfs

`graph` 에 연결된 노드들을 쭉 저장해준다

`queue` 는 0 부터 시작하고
pop(0) 한 노드 `i` 와 연결된 노드들은 모두 `queue` 에 저장

한번 본 애들은 `is_visited` 를 `True` 로 설정하고
거리 길이도 `distances[i] + 1` 로 update

그러면 최종적으로 모든 노드들의 거리가 계산되고
그 중에 최댓값을 찾아서 count 해준 값을 return

![](https://images.velog.io/images/jsh5408/post/af8b2447-5a91-4f70-be0e-2254c2b8ea8f/image.png)