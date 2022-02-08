## 1920. 수 찾기 - python3
https://www.acmicpc.net/problem/1920

#### 내 풀이 - 성공
```
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for b in B:
    TF = 0
    l = 0
    r = N-1
    while l <= r:
        m = (l+r) // 2
        if A[m] == b:
            TF = 1
            break
        if A[m] < b:
            l = m+1
        else:
            r = m-1
    if TF:
        print(1)
    else:
        print(0)
```
A 는 정렬해주고 B 의 숫자들마다 이분탐색 돌리기

TF 로 존재하는지 판단해서 존재하면 1 출력, 아니면 0 출력

![](https://images.velog.io/images/jsh5408/post/29d543e7-22bd-45e0-92cd-d078a07bb54c/image.png)