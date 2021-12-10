## 10845. 큐 - python3
https://www.acmicpc.net/problem/10845

#### 내 풀이 - 성공
```
from sys import stdin
import collections

N = int(stdin.readline())

queue = collections.deque()

for _ in range(N):
    cmd = stdin.readline().split()
    
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
```
deque 를 이용해서 queue 를 만들고
주어진 명령에 따라 각자 역할 수행

pop 할 때는 popleft 를 이용하고
front 는 0 번째, back 은 -1 번째를 출력했다.

![](https://images.velog.io/images/jsh5408/post/706b2964-4c12-4de2-9e06-ef4a55a2e1aa/image.png)