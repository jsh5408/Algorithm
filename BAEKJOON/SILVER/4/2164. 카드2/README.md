## 2164. 카드2 - python3
https://www.acmicpc.net/problem/2164

#### 내 풀이 - 성공
```
from sys import stdin
from collections import deque

N = int(stdin.readline())

nums = deque([i for i in range(1, N+1)])
flag = 0
while len(nums) > 1:
    n = nums.popleft()
    if flag:
        nums.append(n)
        flag = 0
    else:
        flag = 1
print(nums[0])
```
처음에 좀 어렵게 생각해서 규칙을 찾으려 했는데 실패하고...^^
그냥 deque 사용해서 문제 고대로 풀었더니 통과했다

1 ~ N 까지의 숫자들을 nums 에 모두 저장하고
nums 에 1 개의 숫자만 남을 때까지 버리기 & 맨밑으로 반복

flag 가 0 이면 버리고
flag 가 1 이면 맨 밑으로 => append(n)

> deque 를 사용해야 하는 이유
**pop(0) : O(n)
popleft() : O(1)**

> **카드2 의 규칙**
=> `{N - (N 미만의 가장 큰 2 의 제곱)} * 2`
ex)
3 : `(3 - 2) * 2 = 2` => 3 미만의 가장 큰 2 의 제곱 == 2
4 : `(4 - 2) * 2 = 4` => 4 미만의 가장 큰 2 의 제곱 == 2
5 : `(5 - 4) * 2 = 2` => 5 미만의 가장 큰 2 의 제곱 == 4

![](https://images.velog.io/images/jsh5408/post/48aa0b43-5a83-4bc7-a020-91711d7a06ba/image.png)