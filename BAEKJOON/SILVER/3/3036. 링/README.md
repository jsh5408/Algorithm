## 3036. 링
https://www.acmicpc.net/problem/3036

#### GCD - 성공
```
from sys import stdin

N = int(stdin.readline())
rings = list(map(int, stdin.readline().split()))

def gcd(a, b):
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

for i in range(1, N):
    g = gcd(rings[0], rings[i])
    A = rings[0]//g
    B = rings[i]//g
    print(str(A) + "/" + str(B))
```
비교 기준인 첫번째링과 나머지 링들 사이의 최대공약수를 구하는 것이 핵심이다
최대공약수(gcd)를 구하는 정석적인 방법이 생각나지 않아서 비교 대상인 숫자부터 역순으로 확인했다,,

![](https://velog.velcdn.com/images/jsh5408/post/2a25005b-4a50-4319-8cd0-6154c9451304/image.png)

#### GCD 2 - 성공
```
from sys import stdin

N = int(stdin.readline())
rings = list(map(int, stdin.readline().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(1, N):
    g = gcd(rings[0], rings[i])
    A = rings[0]//g
    B = rings[i]//g
    print(str(A) + "/" + str(B))
```

> **최대공약수(gcd)**
```
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

알아두자!!!

![](https://velog.velcdn.com/images/jsh5408/post/d913ce4b-59c3-464d-93d8-cda5ddb0ab80/image.png)
