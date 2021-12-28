## 2579. 계단 오르기 - python3
https://www.acmicpc.net/problem/2579

#### 내 풀이 - 시간 초과
```
import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
stairs = [0]*N

for i in range(N):
    n = int(sys.stdin.readline())
    stairs[i] = n

ans = 0

def func(idx, score, flag):
    global ans
    if N-1 == idx:
        ans = max(ans, score+stairs[idx])
        return
    if N-1 < idx:
        return
    
    if flag:
        func(idx+1, score+stairs[idx], 0)
    func(idx+2, score+stairs[idx], 1)

func(0, 0, 1)
print(ans)
```
재귀 함수로 한칸 움직인 경우, 두칸 움직인 경우 모두 확인

인덱스로 계단 칸수 구분
flag 로 이미 두번 연속했는지 구분

끝까지 다 올라왔을 때만 ans update

하지만 역시나 시간 초과...ㅎ

#### 내 풀이 - 실패
```
from sys import stdin

N = int(stdin.readline())
stairs = [0]*N
dp = [(0, 0)]*N

for i in range(N):
    n = int(stdin.readline())
    stairs[i] = n

ans = stairs[-1]
dp[-1] = (stairs[-1], 1)

for i in range(N-2, -1, -1):
    tmp = 0
    flag = 0
    if i+1 < N and dp[i+1][1]:
        tmp = max(tmp, dp[i+1][0])
        flag = 0
    if i+2 < N and dp[i+2][1]:
        tmp = max(tmp, dp[i+2][0])
        flag = 1
    dp[i] = (tmp+stairs[i], flag)

for v, f in dp:
    if ans < v:
        ans = v

print(ans)
```
dp 를 사용해봤다

맨 마지막 값은 무조건 밟아야하니까 맨 마지막 값부터 역으로 봄

dp = [최대 점수, 연속 여부] 의 형태로 저장

한칸 움직일 경우와 두칸 움직일 경우 중 최댓값 = tmp
dp = [tmp+현재 스코어, flag]

항상 첫번째 계단부터 올라오지 않았을 수도 있으므로 최댓값 찾아서 ans update
(0번째, 1번째의 값만 비교해도 됨)

하지만 실패...

#### 다른 사람의 풀이
```
from sys import stdin

N = int(stdin.readline())
stairs = [0]*N
dp = [0]*N

for i in range(N):
    n = int(stdin.readline())
    stairs[i] = n

if N == 1:
    print(stairs[0])
elif N == 2:
    print(max(stairs[0]+stairs[1], stairs[1]))
else:
    dp[0] = stairs[0]
    dp[1] = max(stairs[0]+stairs[1], stairs[1])
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i]+stairs[i-1])

    print(dp[-1])
```
N 이 1, 2 일 때는 예외 처리 해주기 => IndexError 방지

나머지는 dp 를 이용하는데 그 중 맨 앞 3 개의 값만 직접 처리해줌
0 번째는 0 번째 점수
1 번째는 0+1 점수와 1 번째 점수 중 큰 값
2 번째는 0+2 점수와 1+2 점수 중 큰 값
으로 초기화

그 외의 숫자들은 **두칸 움직인 경우**와 **한칸 움직인 경우** 중 최댓값으로 update
두칸 움직인 경우) dp[i-2] + 현재 스코어
한칸 움직인 경우) 바로 전 계단의 스코어 + dp[i-3] + 현재 스코어
=> 세번 연속으로 할 수 없으므로 전 스코어에서 두칸 전의 값을 가져옴

![](https://images.velog.io/images/jsh5408/post/5e65abd7-d131-4251-b5ca-7bd3ee6f3bae/image.png)