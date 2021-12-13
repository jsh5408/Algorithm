## 10250. ACM 호텔
https://www.acmicpc.net/problem/10250

#### 내 풀이 - 성공
```
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    H, W, N = map(int, stdin.readline().split())
    YY = N % H
    ans = ""
    if YY == 0:
        ans += str(H)
        XX = N // H
    else:
        ans += str(YY)
        XX = N // H + 1
    if XX < 10:
        ans += "0" + str(XX)
    else:
        ans += str(XX)
    print(ans)
```
YYXX 의 형태에서 YY 가 우선으로 증가한다는 점을 이용

1 ~ H 까지의 숫자가 계속 반복되므로 최종적인 YY 는 N % H 층

XX 는 H 가 반복된 횟수와 관련있음 => N // H + 1 호

이 때, N % H 가 0 일 때는 맨 꼭대기 층 (H) + N // H 호로 고정해주기

XX 가 한자리 숫자면 앞에 0 을 붙여준다

![](https://images.velog.io/images/jsh5408/post/733cd672-7226-486c-ae42-a93a4c1d447b/image.png)