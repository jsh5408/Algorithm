## 10773. 제로 - python3
https://www.acmicpc.net/problem/10773

#### 내 풀이 - 성공
```
from sys import stdin

K = int(stdin.readline())
stack = []

for _ in range(K):
    num = int(stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
```
stack 을 이용해서 계속 append 하다가 0 이면 pop 하도록 함
stack 의 합 print

![](https://images.velog.io/images/jsh5408/post/154c8d23-9644-40b2-86c0-135738b906a3/image.png)