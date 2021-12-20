## 15650. N과 M (2) - python3
https://www.acmicpc.net/problem/15650

#### 내 풀이 - 성공
```
from sys import stdin

N, M = map(int, stdin.readline().split())
nums = [i for i in range(1, N+1)]

def func(n, comb):
    if len(comb) == M:
        for c in comb:
            print(c, end=' ')
        print()
        return
    
    for i in range(len(n)):
        func(n[i+1:], comb+[n[i]])

func(nums, [])
```
**15649. N과 M (1)** 에서 재귀 돌리는 부분만 수정

현재 숫자보다 작은 값은 다시 추가할 필요가 없음
=> 그 조합은 이미 사용됐으므로

![](https://images.velog.io/images/jsh5408/post/8d40f976-d100-4253-9cff-8124311e42f6/image.png)