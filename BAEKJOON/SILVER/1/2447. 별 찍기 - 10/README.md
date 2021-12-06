## 2447. 별 찍기 - 10 - python3
https://www.acmicpc.net/problem/2447

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())

arr = [["*"]*N for i in range(N)]

def func(si, sj, ei, ej, n):
    if si == ei or sj == ej:
        return

    tmp = n // 3
    
    for i in range(tmp):
        for j in range(tmp):
            arr[si+tmp+i][sj+tmp+j] = " "
    
    if n != 1:
        func(si, sj, si+tmp, sj+tmp, tmp)
        func(si+tmp, sj, si+tmp*2, sj+tmp, tmp)
        func(si+tmp*2, sj, ei, sj+tmp, tmp)
        
        func(si, sj+tmp, si+tmp, sj+tmp*2, tmp)
        func(si+tmp*2, sj+tmp, ei, sj+tmp*2, tmp)
        
        func(si, sj+tmp*2, si+tmp, ej, tmp)
        func(si+tmp, sj+tmp*2, si+tmp*2, ej, tmp)
        func(si+tmp*2, sj+tmp*2, ei, ej, tmp)

func(0, 0, N, N, N)

for i in range(N):
    for j in range(N):
        print(arr[i][j] ,end='')
    print()
```
3 * 3 기본 모양을 기준으로 분할정복 이용

arr 리스트에 우선 * 로 채워두고
재귀를 돌면서 가운데 부분만 빈칸으로 지워줌

3 분의 1 로 나눈 값을 가지고 9 개의 구역으로 나눠서 재귀 돌리기

![](https://images.velog.io/images/jsh5408/post/fcfdfe65-03ab-445c-86d7-6e7e2b349b36/image.png)