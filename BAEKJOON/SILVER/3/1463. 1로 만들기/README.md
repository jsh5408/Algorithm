## 1463. 1로 만들기 - python3
https://www.acmicpc.net/problem/1463

#### 내 풀이 - 성공
```
N = int(input())

if N == 1:
    print(0)
elif N == 2 or N == 3:
    print(1)
else:
    dp = [0]*(N+1)
    dp[2], dp[3] = 1, 1

    for n in range(4, N+1):
        tmp = n
        if n % 3 == 0:
            tmp = min(tmp, dp[n//3]+1)
        if n % 2 == 0:
            tmp = min(tmp, dp[n//2]+1)
        tmp = min(tmp, dp[n-1]+1)
        dp[n] = tmp

    print(dp[n])
```
dp 를 이용해서 1 ~ N 까지의 숫자들의 최소 연산값을 저장

3 으로 나눠 떨어지는 경우, 2 로 나눠 떨어지는 경우, 1 만 뺐을 경우
세가지를 모두 비교해서 최솟값으로 dp 값 설정

어떤 숫자든지 자기 자신보다 작은 숫자들의 dp 값은 이미 구해져있다는 점을 이용

참고) 처음엔 재귀로 3, 2, 1 세가지 경우를 모두 계산해서 최솟값을 찾았더니 시간 초과가 났다...

![](https://images.velog.io/images/jsh5408/post/92da50e8-0f94-4abb-b205-db181aefd34d/image.png)