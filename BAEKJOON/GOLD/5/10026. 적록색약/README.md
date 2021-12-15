## 10026. 적록색약 - python3
https://www.acmicpc.net/problem/10026

#### 내 풀이 - 성공
```
from sys import stdin
import sys
sys.setrecursionlimit(10**6)

N = int(stdin.readline())
painting = []

for _ in range(N):
    p = list(map(str, stdin.readline().strip()))
    painting.append(p)

a, b = 0, 0

def func(i, j, p):
    if p == "B" or p == "O":
        painting[i][j] = "X"
    else:
        painting[i][j] = "O"
    
    if i-1 >= 0 and painting[i-1][j] == p:
        func(i-1, j, p)
    if j-1 >= 0 and painting[i][j-1] == p:
        func(i, j-1, p)
    if i+1 < N and painting[i+1][j] == p:
        func(i+1, j, p)
    if j+1 < N and painting[i][j+1] == p:
        func(i, j+1, p)

for i in range(N):
    for j in range(N):
        now = painting[i][j]
        if painting[i][j] != "X" and painting[i][j] != "O":
            func(i, j, now)
            a += 1
            if now == "B":
                b += 1

for i in range(N):
    for j in range(N):
        if painting[i][j] == "O":
            func(i, j, "O")
            b += 1

print(a, b)
```
painting 에 입력받은 그림의 정보를 모두 저장

이중 for 문을 돌려서 일반 사람은 RGB 를 모두 구분해서 카운팅 하도록 하고
이 때, 확인한 R, G 는 O 로 바꾸고 B 는 X 로 바꿔주었다.
B 는 적록색약인 사람도 구분하기 때문에 b + 1 도 진행

적록색약인 사람은 R, G 를 구분하지 못하므로 같은 것으로 생각해야함
=> 앞에서 이미 둘 다 O 로 바꿔줬기 때문에 O 의 개수만 세면 된다.

![](https://images.velog.io/images/jsh5408/post/d21678a5-f369-4f02-a6ae-f8b747d3e63b/image.png)