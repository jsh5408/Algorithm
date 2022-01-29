## 2108. 통계학 - python3
https://www.acmicpc.net/problem/2108

#### 내 풀이 - 성공
```
from sys import stdin
import collections
import math

N = int(stdin.readline())
nums = [0] * N

for i in range(N):
    nums[i] = int(stdin.readline())

nums.sort()

# 산술평균
print(round(sum(nums)/N))

# 중앙값
print(nums[N//2])

# 최빈값
n = collections.Counter(nums)
m = 1
for k,v in n.items():
    if v > m:
        m = v
r = []
for k,v in n.items():
    if v == m:
        m = v
        r.append(k)
        if len(r) == 2:
            r.pop(0)
            break
print(r[0])

# 범위
print(nums[-1] - nums[0])
```
입력받은 숫자들은 nums 에 모두 저장한 후 sort()

**산술평균** : N개의 수들의 합을 N으로 나눈 값
round() 함수로 소수점 이하 첫째 자리에서 반올림하도록 함

**중앙값** : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
N 은 무조건 홀수이므로 2 로 나눈 중간값 print

**최빈값** : N개의 수들 중 가장 많이 나타나는 값
Counter 로 숫자들의 빈도수를 파악한 후, 최대 빈도수 m 구하기
다시 값들을 보면서 m 과 같은 값들은 r 에 저장
"여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력" 해야 하므로
길이가 2 개가 되면 break

**범위** : N개의 수들 중 최댓값과 최솟값의 차이
마지막 값 - 처음 값

![](https://images.velog.io/images/jsh5408/post/c8dfd7f0-f6b5-42b8-bf86-d0aca987c6db/image.png)

> **최빈값 다른 풀이**
```
ncnt = collections.Counter(nums).most_common()
if len(ncnt) > 1 and ncnt[0][1] == ncnt[1][1]:
    print(ncnt[1][0])
else:
    print(ncnt[0][0])
```
**most_common()** : 데이터의 개수가 많은 순으로 정렬된 배열 return
ex) `'hello world'`
=> `[('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]`
>
**most_common(1)** : 최대 빈도수의 값 return
ex) `('l', 3)`
>
![](https://images.velog.io/images/jsh5408/post/e92011cc-83f3-46e4-8396-eb87ddb2bdb7/image.png)