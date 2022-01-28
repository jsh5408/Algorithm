## 1764. 듣보잡 - python3
https://www.acmicpc.net/problem/1764

#### 내 풀이 - 성공
```
from sys import stdin

N, M = map(int, stdin.readline().split())

names = set()
ans = []

for _ in range(N):
    p = stdin.readline().strip()
    names.add(p)

for _ in range(M):
    p = stdin.readline().strip()
    if p in names:
        ans.append(p)

ans.sort()

print(len(ans))
for p in ans:
    print(p)
```
듣도 못한 사람은 names 에 저장하고
보도 못한 사람은 입력받을 때마다 names 에 있는지 확인해서 ans 에 저장

사전순으로 정렬하기 위해 sort() 후, 전체 인원과 리스트 print

아니면 set() 의 교집합 연산 이용해서 풀어도 될 듯

![](https://images.velog.io/images/jsh5408/post/d065df8e-11a2-4e2f-b74f-61f84b8ed121/image.png)