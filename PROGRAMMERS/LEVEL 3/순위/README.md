## 순위
https://programmers.co.kr/learn/courses/30/lessons/49191

#### 내 풀이 - 실패
```
def solution(n, results):
    answer = 0
    
    win = {i:[] for i in range(1, n+1)}
    lose = {i:[] for i in range(1, n+1)}
    for a, b in results:
        win[a].append(b)
        lose[b].append(a)
    
    for i in range(1, n+1):
        winner = set(win[i])
        for w in win[i]:
            winner |= set(win[w])
        win[i] = list(winner)
        loser = set(lose[i])
        for l in lose[i]:
            loser |= set(lose[l])
        lose[i] = list(loser)
    
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
    
    return answer
```
각 숫자마다 이긴 사람과 진 사람을 모두 저장 => `win`, `lose`

자신이 이긴 사람과 연결된 사람들까지 모두 더해줌, 연결된 진 사람도 마찬가지

마지막에 이긴 사람과 진 사람의 수가 `n-1` 이라면 순위가 정해진 것이므로 `answer + 1`

하지만 모두 통과하진 못했다..ㅎ

![](https://images.velog.io/images/jsh5408/post/89c72a0b-a8c4-4fa3-a1ca-0694d0102510/image.png)

#### 다른 사람의 풀이
```
from collections import defaultdict

def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
        
    return answer
```
똑같이 `win`, `lose` 를 구해주는데 set 를 이용

`win` : `i` 가 이긴 애들
`lose` : `i` 를 이긴 애들

헷갈리지 않게 주의!!

`i` 를 이긴 사람들은 `i` 한테 진 애들도 이긴 것이므로 `win[winner].update(win[i])`
`i` 한테 진 사람들은 `i` 를 이긴 애들한테도 진 것이므로 `lose[loser].update(lose[i])`

![](https://images.velog.io/images/jsh5408/post/e1fe5199-b6f9-4c49-aa4e-43981af935f6/image.png)