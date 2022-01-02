## 1931. 회의실 배정 - python3
https://www.acmicpc.net/problem/1931

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())

arr = []
for i in range(N):
    a = list(map(int, stdin.readline().split()))
    arr.append(a)

arr.sort(key = lambda x:(x[1], x[0]))

ans = 0
end = 0
for s, e in arr:
    if end <= s or e < end:
        end = e
        ans += 1

print(ans)
```
회의 종료 시간이 관건이므로
회의 시간을 담은 리스트 arr 을 **종료 시간 기준으로 정렬**
=> 종료 시간이 우선이되 시작 시간도 정렬되어야 함

그리고 회의 시간을 하나씩 보면서
종료시간이 현재 범위에 포함되지 않으면 같은 룸에서 회의가 가능하다는 것이므로 ans + 1

전에 leetcode 에선 못 풀었던 것 같은데 이번엔 풀어서 굿~

![](https://images.velog.io/images/jsh5408/post/5bf7a52f-c8f1-42c7-895e-ba92b34d5f0e/image.png)