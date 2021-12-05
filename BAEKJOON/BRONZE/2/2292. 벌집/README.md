## 2292. 벌집 - python3
https://www.acmicpc.net/problem/2292

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())

r = 1
a = 6
while r < N:
    r += a
    a += 6

print(a // 6)
```
이건 무조건 규칙 문제다 싶어서 열심히 규칙을 찾아봤다

1 을 둘러싼 **둘레**가 관건이었음
각 둘레마다 n+1 개의 방을 지나가며 이게 최소 개수가 된다
(1 도 하나의 방에 포함되므로 n+1)

첫번째 둘레 => 2 ~ 7 => 6개의 숫자
두번째 둘레 => 8 ~ 19 => 12개의 숫자
세번째 둘레 => 20 ~ 37 => 18개의 숫자
네번째 둘레 => 38 ~ 61 => 24개의 숫자
...로 각 둘레마다 `6*n` 개의 숫자를 가짐

따라서 6 의 배수 a 를 r 에 계속 더해가면서
N 이 어떤 둘레에 속하는지 판단하고 6 으로 나눈 몫 print

![](https://images.velog.io/images/jsh5408/post/f388a1fe-7961-4e8f-9121-fbb48f5feb38/image.png)