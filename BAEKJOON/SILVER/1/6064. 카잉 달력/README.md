## 6064. 카잉 달력 - python3
https://www.acmicpc.net/problem/6064

#### 내 풀이 - 성공 (PyPy3)
```
from sys import stdin

T = int(stdin.readline())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(T):
    M, N, x, y = map(int, stdin.readline().split())
    a, b = x, y
    lcm = M*N // gcd(M, N)
    while a != b:
        if a < b:
            a += M
        else:
            b += N
        if a > lcm or b > lcm:
            a = -1
            break
    print(a)
```
x, y 는 결국 M, N 의 나머지 값이라는 점을 생각

하지만 몫은 모르는거니까 x, y 에 각각 M, N 을 더해가면서 값이 같아지는 순간을 찾음

ex) 3, 9 => 33 번째
**3 + 10 (13)** > 9
13 < **9 + 12 (21)**
**13 + 10 (23)** > 21
23 < **21 + 12 (33)**
**23 + 10 (33)** == 33

이 때, a, b 는 최대 M, N 의 최소공배수 (lcm) 까지의 범위로 제한
=> 최소공배수 = `M*N // 최대공약수 (gcd)`
넘어가면 -1 print

![](https://images.velog.io/images/jsh5408/post/d52ab796-7699-4e1a-9d1d-ba30d30d46f2/image.png)

#### 다른 사람의 풀이
```
from sys import stdin

T = int(stdin.readline())

for i in range(T):
    M, N, x, y = map(int, stdin.readline().split())
    ans = -1
    while(x <= M*N):
        if (x-y) % N == 0:	# if x % N == y % N:
            ans = x
            break
        x += M
    print(ans)
```
굳이 최소공배수를 구할 필요 없이 넉넉하게 M * N 까지 봐줘도 됨

그리고 x, y 둘 다 생각할 필요 없이 x 에만 M 을 더해가면 된다
=> x - y 를 N 으로 나눈 나머지가 0 이 되면 됨

![](https://images.velog.io/images/jsh5408/post/4cecc737-0938-4936-96d6-fd1e1659b9ca/image.png)