## 등굣길
https://programmers.co.kr/learn/courses/30/lessons/42898

#### 내 풀이 1 - 실패
```
answer = 0
dp = []

def func(start, end, puddles, cnt):
    global answer, dp
    
    dp[start[0]][start[1]] = dp[start[0]][start[1]] + 1
    
    if start[0] == end[0] and start[1] == end[1]:
        return
    
    if start[0] < end[0] and dp[start[0]+1][start[1]] != -1:
        func([start[0]+1, start[1]], end, puddles, cnt+1)
    if start[1] < end[1] and dp[start[0]][start[1]+1] != -1:
        func([start[0], start[1]+1], end, puddles, cnt+1)

def solution(m, n, puddles):
    global answer, dp
    
    for i in range(n+1):
        dp.append([0]*(m+1))
    
    for a, b in puddles:
        dp[a][b] = -1
    
    func([1, 1], [n, m], puddles, 0)
    answer = dp[n][m]
    
    return answer % 1000000007
```
`dp` 에 웅덩이는 `-1` 로, 나머지는 `0` 으로 초기화

재귀 함수로 각 위치의 경우의 수를 `dp` 에 저장

`dp[n][m]` 가 누적 경우의 수가 됨

But... 런타임과 함께 실패의 피바다...

#### 내 풀이 2 - 실패
```
answer = 0
dp = []

def solution(m, n, puddles):
    global answer, dp
    
    for i in range(n+1):
        dp.append([0]*(m+1))
    
    for a, b in puddles:
        dp[a][b] = -1
    
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == -1:
                continue
            if i > 1 and j > 1 and dp[i-1][j] != -1 and dp[i][j-1] != -1:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]
            elif i > 1:
                dp[i][j] += 1
            elif j > 1:
                dp[i][j] += 1
                
    answer = dp[n][m]
    
    return answer % 1000000007
```
굳이 재귀로 모든 경우를 볼 필요가 없을 것 같아서
그냥 이중 for 문으로 각 위치마다 위, 왼쪽의 값을 더해줌

테스트 케이스만 통과하고 다시 실패의 피바다...

뭔가 풀릴 거 같은데 잘 안됐다...^^

#### 다른 사람의 풀이
```
def solution(m, n, puddles):
    mapp = [[0] * (m+1) for _ in range(n+1)]
    
    mapp[1][1] = 1
    
    for x in range(1, n+1):
        for y in range(1, m+1):
            if x == 1 and y == 1:
                continue
                
            if [y, x] in puddles:
                mapp[x][y] = 0
            else:
                mapp[x][y] = mapp[x-1][y] + mapp[x][y-1]
    
    return mapp[-1][-1] % 1000000007
```
내가 구현하고자 한 논리와 가장 유사한 풀이

`(n+1) * (m+1)` 크기의 `mapp` 만들어서 `0` 으로 초기화

이중 for 문 돌려서 맨 처음 시작 값만 제외하고
나머지 좌표가 웅덩이의 좌표인지 확인해서 웅덩이면 `0` 아니면 왼쪽, 위쪽 값 더하기

가장 마지막 위치의 `mapp` 값을 `1000000007` 로 나눈 나머지 return

어렵게 생각할 필요가 없었다...!!

> 참고) https://bladejun.tistory.com/65

![](https://images.velog.io/images/jsh5408/post/bcbfd74c-ab05-49e4-a661-2212df55599e/image.png)