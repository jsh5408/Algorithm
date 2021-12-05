## 9095. 1, 2, 3 더하기
https://www.acmicpc.net/problem/9095

#### 내 풀이 - 성공
```
from sys import stdin

T = int(stdin.readline())
cases = set()

def func(n, t):
    if n == 0:
        cases.add(t)
    elif n < 0:
        return
    
    func(n-1, t+"1")
    func(n-2, t+"2")
    func(n-3, t+"3")

for _ in range(T):
    n = int(stdin.readline())
    cases = set()
    func(n, "")
    print(len(cases))
```
cases set 를 만들어서
1, 2, 3 을 각각 뺀 경우를 재귀로 돌리고
완성된 조합 (n == 0) 을 cases 에 저장하고 길이 print

![](https://images.velog.io/images/jsh5408/post/cb5957d5-f7b1-4406-8bb7-751bc1bd1c8e/image.png)

#### 다른 사람의 풀이
```
from sys import stdin

T = int(stdin.readline())

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return func(n-1) + func(n-2) + func(n-3)

for _ in range(T):
    n = int(stdin.readline())
    print(func(n))
```
dp 이용

1 ~ 5 정도까지 직접 계산해보면
**f(n) = f(n-1) + f(n-2) + f(n-3)**
의 점화식을 얻을 수 있다.

dp 리스트를 직접 만들어 더하는 것도 가능

![](https://images.velog.io/images/jsh5408/post/1331ad38-f656-4143-b87c-638045b16e26/image.png)
