## 15651. N과 M (3) - python3
https://www.acmicpc.net/problem/15651

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
        func(n, comb+[n[i]])

func(nums, [])
```
**15649. N과 M (1)** 에서 재귀 돌리는 부분만 수정

중복으로 사용해도 되므로 슬라이싱 없이 n 리스트를 그대로 다음 재귀로 넘겨줌

![](https://images.velog.io/images/jsh5408/post/2e7997c8-89bf-42cc-a385-c7ccc21a95cd/image.png)