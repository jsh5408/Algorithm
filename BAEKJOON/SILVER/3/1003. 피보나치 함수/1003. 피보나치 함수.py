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