## 9375. 패션왕 신해빈 - python3
https://www.acmicpc.net/problem/9375

#### 내 풀이 - 성공
```
from sys import stdin
import collections

N = int(stdin.readline())

for _ in range(N):
    n = int(stdin.readline())
    clothes = collections.defaultdict(int)
    ans = 1
    for _ in range(n):
        cloth = stdin.readline().split()
        clothes[cloth[1]] += 1
    for k, v in clothes.items():
        ans *= v+1
    print(ans-1)
```
모든 의상 종류마다 착용하지 않는 경우도 추가해서 계산

의상의 이름은 상관이 없으므로 (같은 이름의 의상이 입력으로 들어오지도 않음)
의상의 개수만 세서 clothes 에 저장

ans 는 1 로 초기화하고
의상 개수 + 1 (착용 X 의 경우) 을 모두 곱해준 후
알몸일 경우 한가지를 빼주고 print

![](https://images.velog.io/images/jsh5408/post/b7e5170a-2cfa-47e6-86ff-94873c2ae7a8/image.png)