## 타겟 넘버
https://programmers.co.kr/learn/courses/30/lessons/43165

#### 내 풀이 - 통과
```
def func(numbers, target, t):
    if len(numbers) == 0:
        if t == target:
            return 1
        return 0
    
    ans = 0
    ans += func(numbers[1:], target, t+numbers[0])
    ans += func(numbers[1:], target, t-numbers[0])
    
    return ans

def solution(numbers, target):
    answer = 0
    
    answer = func(numbers, target, 0)
    
    return answer
```
`numbers` 숫자들을 0 인덱스부터 하나씩
`t` 에 더하는 방법 & 빼는 방법 두가지의 경우로 재귀 돌림

![](https://images.velog.io/images/jsh5408/post/adeeef03-1769-47db-8c99-3611d278a290/image.png)