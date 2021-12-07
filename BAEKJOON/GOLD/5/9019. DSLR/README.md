## 9019. DSLR - python3
https://www.acmicpc.net/problem/9019

#### 내 풀이 - 시간 초과
```
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    A, B = map(str, stdin.readline().split())
    ans = ""
    while A != B:
        nextA = A
        diff = 10000
        DSLR = ""
        
        d = (int(A) * 2) % 10000
        s = int(A)-1 if int(A) > 0 else 9999
        l = int(A[1:]+A[0])
        r = int(A[-1]+A[:-1])
        
        if d > 0 and diff > abs(int(B) - d):
            nextA = str(d)
            diff = abs(int(B) - d)
            DSLR = "D"
        if s > 0 and diff > abs(int(B) - s):
            nextA = str(s)
            diff = abs(int(B) - s)
            DSLR = "S"
        if l > 0 and diff > abs(int(B) - l):
            nextA = str(l)
            diff = abs(int(B) - l)
            DSLR = "L"
        if r > 0 and diff > abs(int(B) - r):
            nextA = str(r)
            diff = abs(int(B) - r)
            DSLR = "R"
            
        ans += DSLR
        A = nextA
    print(ans)
```
A 와 B 가 같아질 때까지 반복문 돌려서 DSLR 값 확인

현재 A 로 d, s, l, r 을 모두 구해 그 중에 B 와 가장 가까운 값을 찾음
ans 에 DSLR 연산을 저장하고 A 는 바뀐 값으로 update

하지만... 시간초과...

> <문제점>
1. **123 의 R 연산 => 312 (X), 3012 (O)** 의 경우 고려 X
2. 문자열 연산으로 시간이 더 걸림
3. B 와 가장 가까운 값은 상관이 없는 듯

#### 다른 사람의 풀이 (PyPy3)
```
from sys import stdin
from collections import deque

def bfs(start, end):
    q = deque([[start, ""]])
    visited = [0] * 10000
    visited[start] = True

    while q:
        num, operation = q.popleft()

        if num == end:
            return operation

        # D
        if not visited[num * 2 % 10000]:
            visited[num * 2 % 10000] = True
            q.append([num * 2 % 10000, operation + "D"])
        # S
        if not visited[(num - 1) % 10000]:
            visited[(num - 1) % 10000] = True
            q.append([(num - 1) % 10000, operation + "S"])
        # L
        if not visited[num % 1000 * 10 + num // 1000]:
            visited[num % 1000 * 10 + num // 1000] = True
            q.append([num % 1000 * 10 + num // 1000, operation + "L"])
        # R
        if not visited[num % 10 * 1000 + num // 10]:
            visited[num % 10 * 1000 + num // 10] = True
            q.append([num % 10 * 1000 + num // 10, operation + "R"])

T = int(stdin.readline())

for _ in range(T):
    A, B = map(int, stdin.readline().split())
    print(bfs(A, B))
```
BFS 이용

[현재 A, DSLR 연산] 의 형태로 q 에 저장
visited 를 이용해서 본 숫자들은 모두 True

처음 보는 숫자들은 DSLR 연산 진행 후 q 에 모두 저장
하나씩 pop 하면서 해당 숫자로부터 B 로 가는게 가능한지 수행
가장 먼저 end 와 같아지는 숫자가 있다면 operation print

![](https://images.velog.io/images/jsh5408/post/4854e618-0e7b-4946-a1e8-d851e23ca921/image.png)