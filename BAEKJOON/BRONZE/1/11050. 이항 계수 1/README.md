## 11050. 이항 계수 1 - python3
https://www.acmicpc.net/problem/11050

#### 내 풀이 - 성공
```
from sys import stdin

N, K = map(int, stdin.readline().split())

ans = 1
for i in range(N-K+1, N+1):
    ans *= i

for i in range(1, K+1):
    ans //= i

print(ans)
```

> **이항 계수 수식 이용**
![](https://images.velog.io/images/jsh5408/post/2be6104a-122a-439b-9c1a-5d8818702b33/image.png)

n! 을 구한 후, k! 과 (n-k)! 으로 나누는 것보다는
n * (n-1) * ... * (n-k+1) 을 구하고 k! 으로 나누는 게
반복문도 3 개에서 2 개로 줄고 더 빠르게 구현됐다

![](https://images.velog.io/images/jsh5408/post/0b1f8a00-6602-4272-8c48-eabcc491041b/image.png)

#### 다른 사람의 풀이
```
from sys import stdin

N, K = map(int, stdin.readline().split())

def func(N):
    if N <= 1:
        return 1
    
    return N * func(N-1)

print(func(N) // (func(K) * func(N-K)))
```
팩토리얼 함수 func 을 직접 구현해서
nCk 공식 그대로 출력하는 방식

![](https://images.velog.io/images/jsh5408/post/3d9127b8-fa09-4fb2-8fcb-dd81c1907603/image.png)

#### 다른 사람의 풀이 2
```
from sys import stdin
from math import factorial

N, K = map(int, stdin.readline().split())

print(factorial(N) // (factorial(K) * factorial(N-K)))
```
math.factorial 을 이용

![](https://images.velog.io/images/jsh5408/post/28e3d09e-107a-44f7-b2f0-84e3d4b6100e/image.png)