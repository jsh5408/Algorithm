## 1003. 피보나치 함수
https://www.acmicpc.net/problem/1003

#### 내 풀이 - 성공
```
zero = 0
one = 0

# dp[n] = [zero, one, value]
dp = {}

dp[0] = [1, 0, 0]
dp[1] = [0, 1, 1]

def fibonacci(n):
  global zero, one, dp

  if n in dp:
    zero += dp[n][0]
    one += dp[n][1]
    return dp[n][2]
  else:
    value = fibonacci(n-1) + fibonacci(n-2)
    dp[n] = [zero, one, value]
    return value

T = int(input())
cases = []
for i in range(T):
  n = int(input())
  cases.append(n)

for c in cases:
  fibonacci(c)
  print(zero, one)
  zero = 0
  one = 0
```
`dp[n] = [zero, one, value]` 의 형태로 저장
=> `[0 의 개수, 1 의 개수, 피보나치 값]`

0, 1 의 경우는 미리 저장해두고
입력받은 케이스들 모두 `fibonacci` 함수 돌리면서
각 숫자들의 `dp` 저장
=> 이미 본 숫자들은 `dp` 값을 가져와서 사용

![](https://images.velog.io/images/jsh5408/post/1b440d0a-74b5-48b9-ba92-f91b8a16360a/image.png)
