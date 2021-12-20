## 15652. N과 M (4) - python3
https://www.acmicpc.net/problem/15652

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
        func(n[i:], comb+[n[i]])

func(nums, [])
```
**15649. N과 M (1)** 에서 재귀 돌리는 부분만 수정

중복으로 사용해도 되지만 비내림차순이어야 하므로
i 번째의 값을 포함해서 다음 재귀로 넘겨줌
=> 다음 수열의 값으로 i 이상의 값들만 오게 됨

![](https://images.velog.io/images/jsh5408/post/4890aef1-95b9-417b-96be-26319285a016/image.png)