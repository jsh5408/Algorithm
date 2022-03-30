## 정수 삼각형
https://programmers.co.kr/learn/courses/30/lessons/43105

#### 내 풀이 - 통과
```
def solution(triangle):
    answer = 0
    
    dp = []
    for i in range(len(triangle)):
        dp.append([0]*len(triangle[i]))
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j]+triangle[i][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = dp[i-1][j-1]+triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j])
    
    return max(dp[-1])
```
`triangle` 과 같은 크기의 `dp` 생성

`dp[i-1][j-1]` 과 `dp[i-1][j]` 중에 큰 값으로 update

마지막 줄의 최댓값 return

![](https://images.velog.io/images/jsh5408/post/db85c513-16b3-483d-b8f8-e5a30b2777a7/image.png)