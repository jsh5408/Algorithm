## 섬 연결하기
https://programmers.co.kr/learn/courses/30/lessons/42861

#### 내 풀이 - 실패
```
answer = float('inf')

def solution(n, costs):
    ### 그래프처럼 섬 연결 => dic 에 저장 ###
    dic = {i:[] for i in range(n)}
    for a, b, c in costs:
        dic[a].append((b, c))
        dic[b].append((a, c))
        
    ### 재귀로 최소 cost 찾기 ###
    def func(start, end, cost, path, n):
        global answer
        if start == end:
            ### 모든 지점을 다 지났을 때의 최솟값을 answer 에 저장 ###
            if len(path) == n:
                answer = min(answer, cost)
            return cost
        
        ans = float('inf')
        for i, c in dic[start]:
            if i not in path:
                ans = min(ans, func(i, end, cost+c, path+[i], n))
        return ans
    
    ### 섬 개수만큼 dp 생성 ###
    dp = []
    for i in range(n):
        dp.append([float('inf')]*n)
        
    for i in range(n):
        for j in range(i+1, n):
            dp[i][j] = func(i, j, 0, [i], n)
    
    return answer
```
1. 그래프처럼 섬들을 연결해서 `dic` 에 저장

2. 재귀 함수로 각 섬들 사이의 최소 cost 를 구해서 return => `dp` 에 저장
`answer` 는 모든 지점을 다 지났을 때의 최솟값으로 update

`dp` 를 이용하려 했으나 시간 부족으로 실패...

![](https://images.velog.io/images/jsh5408/post/f4466b2b-f81f-49c1-bc05-873d80baf742/image.png)

#### 다른 사람의 풀이
```
def solution(n, costs):
    ans = 0
    costs.sort(key = lambda x: x[2])
    routes = set([costs[0][0]])
    
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans
```
kruskal algorithm 을 이용해야 한다...

`costs` 는 cost 값 기준으로 정렬
`costs[0][0]` 를 초기값으로 갖는 set 선언 => `routes`

모든 섬들이 `routes` 에 포함될 때까지 반복문 돌리기
둘 중 하나의 섬만 `routes` 에 있을 경우엔 나머지 섬도 `routes` 에 넣어주고
`ans` 에 `cost` 값 더해준 후, 다리를 지났다는 의미로 `[-1, -1, -1]` 로 변경

외우자!!!

![](https://images.velog.io/images/jsh5408/post/2b4f5827-d48e-4f1a-b39c-3ae1e5f107a5/image.png)