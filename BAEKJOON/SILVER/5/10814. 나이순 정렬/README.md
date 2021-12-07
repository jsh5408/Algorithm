## 10814. 나이순 정렬 - python3
https://www.acmicpc.net/problem/10814

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())
member = []

for i in range(N):
    age, name = stdin.readline().split()
    member.append((i, int(age), name))

member.sort(key = lambda x : (x[1], x[0]))

for m in member:
    print(str(m[1]) + " " + m[2])
```
(가입순서, 나이, 이름) 의 형태로 member 에 저장
정렬할 때 나이 -> 가입순서 순으로 정렬하도록 함

![](https://images.velog.io/images/jsh5408/post/9db02dcb-7370-402d-83d0-8ba6395e064b/image.png)