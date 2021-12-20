## 2630. 색종이 만들기 - python3
https://www.acmicpc.net/problem/2630

#### 내 풀이 - 성공
```
from sys import stdin
import collections

N = int(stdin.readline())

papers = []
for _ in range(N):
    p = list(map(int, stdin.readline().split()))
    papers.append(p)

white = 0
blue = 0

def func(si, sj, ei, ej, n):
    global white, blue

    value = papers[si][sj]
    cut = 0
    for i in range(si, ei):
        for j in range(sj, ej):
            if value != papers[i][j]:
                cut = 1
                break
        if cut:
            break
    
    if cut:
        func(si, sj, si+n//2, sj+n//2, n//2)  # 1
        func(si, sj+n//2, si+n//2, sj+n, n//2)  # 2
        func(si+n//2, sj, si+n, sj+n//2, n//2)  # 3
        func(si+n//2, sj+n//2, si+n, sj+n, n//2)  # 4
    else:
        if value == 0:
            white += 1
        else:
            blue += 1

func(0, 0, N, N, N)

print(white)
print(blue)
```
func 함수)
현재 구역이 모두 같은 값으로 이뤄져있는지 판단
모두 같은 값이면 white / blue update

다른 값이 하나라도 있으면 break 후 4 등분
=> 전체 길이의 절반 (n//2) 을 (si, sj) 를 기준으로 더함

분할정복을 이용했다

![](https://images.velog.io/images/jsh5408/post/a44af638-da43-4f48-9c91-c5f61db93eb0/image.png)