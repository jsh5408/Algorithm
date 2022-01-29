## 1697. 숨바꼭질 - python3
https://www.acmicpc.net/problem/1697

#### 내 풀이 - 시간초과
```
import sys
sys.setrecursionlimit(10**5)

N, K = map(int, sys.stdin.readline().split())

ans = abs(K-N)
M = N
while M < K:
    M *= 2

def func(n, k, cnt):
    global ans, M
    
    if ans < cnt:
        return
    if n == k:
        ans = min(ans, cnt)
        return

    # 걷기
    if n-1 >= 0 and cnt+1 <= ans:
        func(n-1, k, cnt+1)
    if n+1 <= k and cnt+1 <= ans:
        func(n+1, k, cnt+1)

    # 순간이동
    if n*2 <= M and cnt+1 <= ans:
        func(n*2, k, cnt+1)

func(N, K, 0)
print(ans)
```
우선 ans 는 abs(K-N) 으로 초기화
=> N 이 K 보다 큰 경우를 고려

순간이동의 범위를 제한하기 위해 M 지정
=> N 에 2 를 곱한 값 중 K 보다 큰 첫번째 값

재귀 함수를 돌려서 ans 에 최소 횟수 update
걷기는 0 ~ k 범위이도록 함

하지만 시간 초과...☆

#### 다른 사람의 풀이
```
import sys
import collections

N, K = map(int, sys.stdin.readline().split())

queue = collections.deque()
dist = collections.defaultdict(int)
visited = collections.defaultdict(int)

queue.append(N)
visited[N] = 1

# bfs
while queue:
    node = queue.popleft()
    if node == K:
        print(dist[node])
        break
    for next_node in (node-1, node+1, 2*node):
        if visited[next_node] != 1 and next_node <= 100000:
            queue.append(next_node)
            visited[next_node] = 1
            dist[next_node] = dist[node] + 1
```
deque 를 이용한 queue 생성
dist : 걸린 시간 저장
visited : 봤던 숫자들인지 체크

처음 시작 값인 N 을 queue 에 저장 & visited[N] = 1

반복문을 이용한 bfs 로
지금 node 가 K 라면 print & break
아니라면 `(node-1, node+1, 2*node)` 세가지 경우를 보면서
방문한 노드가 아니고 100000 보다 작을 때만
queue 에 저장 & visited = 1 & dist 값 update

> 참고) https://deep-learning-study.tistory.com/611

![](https://images.velog.io/images/jsh5408/post/de3455e1-2d1e-4f60-a199-bf203a7abf95/image.png)