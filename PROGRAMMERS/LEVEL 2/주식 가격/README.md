## 주식가격
https://programmers.co.kr/learn/courses/30/lessons/42584

#### 내 풀이
정확성: 66.7
효율성: 33.3
합계: 100.0 / 100.0
```
def solution(prices):
    ans = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        ans.append(cnt)
    
    return ans
```
각 숫자마다 자기 자신 이후에 자신보다 작은 값이 나올때까지 `cnt + 1`
작은 값이 나오거나 끝까지 다 봤으면 `ans` 에 append