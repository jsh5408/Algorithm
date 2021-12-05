## 10816. 숫자 카드 2
https://www.acmicpc.net/problem/10816

#### 내 풀이 - 성공
```
from sys import stdin
import collections

N = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

count = collections.Counter(cards)

for n in nums:
    print(count[n], end=" ")
```
N, card, M, nums 를 모두 입력받고
상근이 카드의 count 를 구해서
nums 의 숫자들을 하나씩 보며 count 값 print

![](https://images.velog.io/images/jsh5408/post/a5c00b38-488d-47d4-9c93-bc20794d19a6/image.png)
