## 2869. 달팽이는 올라가고 싶다 - python3
https://www.acmicpc.net/problem/2869

#### 내 풀이 - 성공
```
from sys import stdin
import math

A, B, V = map(int, stdin.readline().split())

if A == V:
    print(1)
else:
    V -= A
    ans = 1
    day = 0
    ans += math.ceil(V / (A-B))
    print(ans)
```
A == V 일 때는 하루면 되니까 1 print

나머지는 A 가 B 보다 크니까 마지막 하루는 A 미터 올라가도록 함 => V -= A & ans = 1
남은 날들은 낮 - 밤 값을 V 로 나누고 올림한 값이므로 모두 더해서 print

![](https://images.velog.io/images/jsh5408/post/4a607de7-ef69-404e-9fda-742c9f9c63c9/image.png)