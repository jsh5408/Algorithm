## 10828. 스택 - python3
https://www.acmicpc.net/problem/10828

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())

stack = []

for _ in range(N):
    cmd = stdin.readline().split()
    
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
```
stack 을 하나 만들고

문제 고대로 조건에 따라 구분

push : append
pop : 가능하다면 pop, 아니면 -1
size : stack 의 크기
empty : 스택이 비어있는지 아닌지 여부
top : 스택의 가장 마지막 값 또는 -1

![](https://images.velog.io/images/jsh5408/post/9d00e35e-2cd7-4845-a1d7-6efc1e586957/image.png)