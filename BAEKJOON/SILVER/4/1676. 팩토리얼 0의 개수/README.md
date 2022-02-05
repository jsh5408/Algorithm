## 1966. 팩토리얼 0의 개수 - python3
https://www.acmicpc.net/problem/1676

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())
ans = 0

five = 5
while five <= N:
    for n in range(five, N+1, five):
        ans += 1
    five *= 5
print(ans)
```
전에 leetcode 에서 비슷한 문제 풀었던 게 생각났다

0 의 개수는 곧 **`2*5 = 10` 의 개수와 관련이 있다**
=> 2 는 5 보다 무조건 많은 개수를 가지니까 생각하지 않고 오직 **5 의 개수만 세주기**

이 때, 25, 50, 75, ... 와 같이 5 가 여러개 있는 숫자 처리 주의
=> `25 = 5 * 5`, `50 = 5 * 5 * 2`, ...

따라서 5 의 제곱수들의 배수까지 모두 세줌

처음엔 5 부터 시작해서 5 의 배수 모두 세주고
그 다음엔 25 (5 의 제곱) 부터 시작해서 25 의 배수 모두 세주고, 125 ...

![](https://images.velog.io/images/jsh5408/post/5899428b-9f90-4cd8-9e30-c7faea86e006/image.png)
