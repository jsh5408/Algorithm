## 17262. Four Squares
https://www.acmicpc.net/problem/17626

#### DP - 성공
```
from sys import stdin
import math

N = int(stdin.readline())
dp = [0]*(N+1)

for i in range(1, N+1):
    tmp = int(math.sqrt(i))
    m = 4
    for j in range(tmp, 0, -1):
        m = min(m, dp[i-j*j] + 1)
    dp[i] = m

print(dp[N])
```

1 ~ N 까지의 숫자들마다 최소 개수의 제곱수 합을 구해줘서 dp 에 저장

이 때, 최대 4 개의 제곱수로 이루어지기 때문에 최대 개수 m 은 4 로 초기화
각 숫자들의 루트 값부터 1 까지 (역순으로) 조합들을 모두 확인해서 최솟값을 찾아준다

![](https://velog.velcdn.com/images/jsh5408/post/4500cd83-ba3b-4e48-97be-b0243c374917/image.png)
