## 2805. 나무 자르기 - python3
https://www.acmicpc.net/problem/2805

#### 내 풀이 - 시간 초과 (Python3) / 통과 (PyPy3)
```
from sys import stdin
import collections

N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

total = sum(trees)
trees.sort()
count = collections.Counter(trees)

if total == M:
    print(0)
else:
    idx = 0
    num = N
    if trees[idx] == 0:
        idx += count[0]
        num -= count[0]
    for t in range(1, max(trees)+1):
        if total - num < M:
            break
        total -= num 
        if t == trees[idx]:
            idx += count[t]
            num -= count[t]

    print(t-1)
```
나무들을 높이 1 씩 잘라감

나무의 전체 높이 합이 M 일 경우 자를 필요가 없으므로 print 0

나머지는 정렬하고
같은 높이의 나무를 알기 위해 Counter 를 구해줌

0 높이의 나무는 미리 제외 => idx, num update

1 부터 최대 높이까지 넉넉하게 범위를 잡고
높이 1 씩 나무를 잘라준다
=> total - 자를 수 있는 나무의 개수

M 보다 작아지면 더 자를 수 없으므로 break

현재 높이가 주어진 나무의 높이와 같아지면
그 다음부턴 해당 나무는 자를 수 없으므로 idx, num update
=> 중복일 경우를 고려해서 count 값만큼 +-

> **PyPy**
- JIT 컴파일러가 포함 되어있어 일반적으로 Python 보다 속도가 빠르다
- Python 보다 메모리 사용량이 많다
>
따라서 Python3 와 PyPy3 를 적절하게 섞어가며 사용해야할 듯

![](https://images.velog.io/images/jsh5408/post/ed852e10-0d4b-442e-a253-2b5d9f71ad36/image.png)

하지만 이분 탐색을 사용하는게 정석!!!

#### 내 풀이 2 - 시간 초과 (Python3) / 통과 (PyPy3)
```
from sys import stdin

N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

total = sum(trees)
trees.sort()

l = 0
r = max(trees)

while l <= r:
    m = (l+r) // 2

    tmp = 0
    for i in range(N):
        if trees[i] >= m:
            break
        tmp += trees[i]	# m 보다 작은 값들
    tmp += m*(N-i)	# 현재 높이 * m 보다 큰 값들의 개수
    
    if total - tmp < M:
        r = m-1
    else:
        l = m+1

print(l-1)
```
이분 탐색 이용

"m 보다 작은 값들" 과 "현재 높이 * m 보다 큰 값들의 개수" 는 total 에서 빼줌
그 값이 M 보다 작으면 더 작게 잘라야하므로 r 변경
크거나 같으면 더 크게 자르기 위해 l 변경

![](https://images.velog.io/images/jsh5408/post/6372a23c-e292-4764-81c8-f37865e01039/image.png)

#### 다른 사람의 풀이
```
from sys import stdin

N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

l = 0
r = max(trees)

while l <= r:
    m = (l+r) // 2

    tmp = 0
    for i in range(N):
        if trees[i] >= m:
            tmp += trees[i] - m
    
    if tmp < M:
        r = m-1
    else:
        l = m+1

print(r)
```
더 깔끔한 이분 탐색

나무들을 정렬하지 않고
자를 수 있는 나무들만 현재 높이만큼 잘라서 tmp 에 저장한 후 M 과 비교

![](https://images.velog.io/images/jsh5408/post/5f58f564-5005-44cc-9784-f5616c78badb/image.png)