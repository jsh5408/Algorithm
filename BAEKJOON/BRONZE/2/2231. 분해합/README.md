## 2231. 분해합 - python3
https://www.acmicpc.net/problem/2231

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())

ans = 0
for n in range(1, N):
    s = str(n)
    M = n
    for c in s:
        M += int(c)
    if M == N:
        ans = n
        break

print(ans)
```
뭔가 규칙을 찾으려 했지만... 안됐고
브루트포스로 하니까 통과됐다

1 ~ N-1 까지의 숫자들이 N 의 생성자가 되는지 일일이 확인
가장 먼저 발견된 생성자가 가장 작으므로 break

>  1 ~ N-1 의 범위는 너무 큰 것 같아서 범위를 줄여봤다
* start = `N - 자릿수*9` => 실패
* start = `N//2` => 통과
![](https://images.velog.io/images/jsh5408/post/e07d4634-af27-47f4-9187-24d7c033d175/image.png)

> 참고) 분해합을 구하는 다른 방식
```
s = list(map(int, str(n)))
M = n + sum(s)
```

![](https://images.velog.io/images/jsh5408/post/4b184178-dc12-45eb-a004-7b626c0e50b1/image.png)
