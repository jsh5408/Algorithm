## 10989. 수 정렬하기 3 - python3
https://www.acmicpc.net/problem/10989

#### 내 풀이 - 성공
```
from sys import stdin
import collections

N = int(stdin.readline())

nums = collections.defaultdict(int)

for i in range(N):
    n = int(stdin.readline())
    nums[n] += 1

nums = sorted(nums.items())

for k, v in nums:
    for _ in range(v):
        print(k)
```
nums 라는 딕셔너리를 이용해서 입력받은 숫자들의 개수를 저장

nums 의 key 를 기준으로 정렬 후 개수 만큼 print

![](https://images.velog.io/images/jsh5408/post/74b4c2d0-a86d-4389-b5b9-e4a694aad31b/image.png)

#### 다른 사람의 풀이
```
from sys import stdin

N = int(stdin.readline())

nums = [0]*10001

for i in range(N):
    n = int(stdin.readline())
    nums[n] = nums[n] + 1

for i in range(10001):
    for j in range(nums[i]):
        print(i)
```
N 의 범위가 10,000 보다 작거나 같은 자연수라고 주어졌으므로
처음부터 nums 의 길이를 10001 로 잡음

인덱스를 숫자로, 배열의 값은 개수로 사용해서 입력받은 숫자의 개수를 모두 저장

10001 개의 숫자들을 모두 보면서 개수만큼 print

정렬 없이 사용할 수 있다!!

![](https://images.velog.io/images/jsh5408/post/fd8f22a5-948d-4a58-8b07-617cdf76af22/image.png)