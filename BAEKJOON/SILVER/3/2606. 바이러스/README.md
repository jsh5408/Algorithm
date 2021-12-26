## 2606. 바이러스 - python3
https://www.acmicpc.net/problem/2606

#### 내 풀이 - 성공
```
from sys import stdin
import collections

N = int(stdin.readline())
C = int(stdin.readline())
network = {i:[] for i in range(1, N+1)}

for i in range(C):
    a, b = map(int, stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

computers = [1]*(N+1)
computers[0] = 0

queue = collections.deque([1])

while queue:
    q = queue.popleft()
    computers[q] = 0
    for n in network[q]:
        if computers[n]:
            queue.append(n)

print(computers.count(0)-2)
```
network 에 서로 연결된 컴퓨터들 저장
computers 에 웜 바이러스 감염 여부 저장
0 번째 인덱스는 사용하지 않으므로 0 으로 초기화

1 번 컴퓨터부터 감염되므로 queue 에 1 저장
하나씩 pop 해서 감염 표시 => computers[q] = 0
연결된 컴퓨터들을 queue 에 append

최종적으로 감염된 컴퓨터의 수는 0 의 개수 - 2
(2 => 의미없는 0 번째 & 시작 값인 1 번째)

![](https://images.velog.io/images/jsh5408/post/0487af0e-41e2-4f15-9b55-f3890570ad41/image.png)