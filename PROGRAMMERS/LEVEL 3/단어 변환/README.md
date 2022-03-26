## 단어 변환
https://programmers.co.kr/learn/courses/30/lessons/43163

#### 내 풀이 - 통과
```
def func(begin, target, words, cnt):
    if begin == target:
        return cnt
    
    if len(words) == 0:
        return 0
    
    ans = float('inf')
    for i in range(len(begin)):
        for j in range(len(words)):
            if begin[:i]+begin[i+1:] == words[j][:i]+words[j][i+1:]:
                ans = min(ans, func(words[j], target, words[:j]+words[j+1:], cnt+1))
    return ans

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    answer = func(begin, target, words, 0)
    
    if answer == float('inf'):
        return 0
    
    return answer
```
우선 `target` 이 `words` 에 존재하지 않으면 return 0

재귀 돌려서 최솟값을 찾아줌
`begin` 의 각 문자들 하나씩 없앤 것과
`words` 값의 각 문자들 하나씩 없앤 것이 같은지 확인
=> 한 글자만 차이가 나는 문자는 다음 재귀로

사용한 단어도 `words` 에서 제외

![](https://images.velog.io/images/jsh5408/post/0b2dcd33-2625-4d83-962a-690191a086e1/image.png)