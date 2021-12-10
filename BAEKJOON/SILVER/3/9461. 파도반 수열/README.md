## 9461. 파도반 수열 - python3
https://www.acmicpc.net/problem/9461

#### 내 풀이 - 성공
```
from sys import stdin
import collections

T = int(stdin.readline())
nums = [0]*100
nums[0], nums[1], nums[2] = 1, 1, 1
nums[3], nums[4] = 2, 2

for i in range(5, 100):
    nums[i] = nums[i-5] + nums[i-1]

for _ in range(T):
    N = int(stdin.readline())
    print(nums[N-1])
```
인덱스 5 이상부터는
**nums[i] = nums[i-5] + nums[i-1]** 의 규칙이 있다는 것을 발견했다.

따라서 0 ~ 4 까지는 직접 초기화를 해주고 (1, 1, 1, 2, 2)
N 이 최대 100 까지이므로 nums[i] 를 모두 구해주고
입력받은 N print

![](https://images.velog.io/images/jsh5408/post/f1925902-df04-4f84-a541-08491b01265b/image.png)