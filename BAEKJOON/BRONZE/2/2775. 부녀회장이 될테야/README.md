## 2775. 부녀회장이 될테야 - python3
https://www.acmicpc.net/problem/2775

#### 내 풀이 - 성공
```
from sys import stdin

T = int(stdin.readline())

dp = []

for i in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())

    nums = [i for i in range(n+1)]
    ans = 0
    for _ in range(k):
        for j in range(1, n+1):
            nums[j] += nums[j-1]
    
    print(nums[-1])
```
0 층은 1 ~ n 호가 있고 i 호는 i 명이 있으므로
nums = [1, 2, 3, ... , n] 로 초기화

**자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합** 을 만족해야하므로
0 층부터 k 층까지 반복해서 누적합을 구해주면 된다

![](https://images.velog.io/images/jsh5408/post/8c805bd3-c5cf-4db8-94fc-414d2fcda55b/image.png)