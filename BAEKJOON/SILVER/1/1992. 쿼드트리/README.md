## 1992. 쿼드트리 - python3
https://www.acmicpc.net/problem/1992

#### 내 풀이 - 성공
```
import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())

mat = []

for i in range(N):
    s = sys.stdin.readline().strip()
    tmp = []
    for c in s:
        tmp.append(int(c))
    mat.append(tmp)

def func(si, sj, ei, ej, n):
    val = mat[si][sj]
    flag = 1

    for i in range(si, ei):
        for j in range(sj, ej):
            if mat[i][j] != val:
                flag = 0
                break
    
    if flag == 1:
        return str(val)
    else:
        # 4등분
        s = "("
        if n//2 > 0:
            s += func(si, sj, si+n//2, sj+n//2, n//2) # 왼위
            s += func(si, sj+n//2, si+n//2, ej, n//2) # 오위
            s += func(si+n//2, sj, ei, sj+n//2, n//2) # 왼아
            s += func(si+n//2, sj+n//2, ei, ej, n//2) # 오아
        return s + ")"

ans = func(0, 0, N, N, N)
print(ans)
```
저번에 분할정복 했던 걸 생각하며 풀었다

우선 mat 에 영상에 대한 정보를 모두 담고 func 이라는 재귀함수를 만들어줬다

시작 인덱스 (si, sj)
끝 인덱스 (ei, ej)
4 등분 할 때 사용할 크기 n
을 매개변수로 함

현재 mat 의 시작 값과 비교해서 모두 같은 값이면 그 값 return
하나라도 다른 값이 있으면 n//2 길이만큼 4 등분 => 괄호 추가

![](https://images.velog.io/images/jsh5408/post/3db21fd9-ac44-400b-a059-5322db47b859/image.png)