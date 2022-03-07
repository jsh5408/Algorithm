## H-Index - Level 2
https://programmers.co.kr/learn/courses/30/lessons/42747

#### 내 풀이 - 통과
```
def solution(citations):
    answer = 0
    citations.sort()
    idx = 0
    
    for i in range(1, max(citations)):
        while idx < len(citations) and citations[idx] < i:
            idx += 1
        if idx <= i and len(citations) - idx >= i:
            answer = max(answer, i)
    
    return answer
```
우선 `citations` 정렬 => sort()

`1 ~ max(citations)` 의 범위에서 H-index 찾기

`citations` 에서의 `i` 위치를 `idx` 로 찾아서
"h 번 이상 인용된 논문이 h 편 이상 & 나머지 논문이 h 번 이하" 인지 확인

![](https://images.velog.io/images/jsh5408/post/5dde5124-7e4e-46a1-afd0-900f9829f113/image.png)

#### 다른 사람의 풀이
```
def solution(citations):
    citations.sort()
    l = len(citations)
    
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    
    return 0
```
더 간단한 천재같은 풀이

정렬 후, "0 ~ `citations` 의 길이" 의 범위만 확인

`if citations[i] >= l-i:`
=> `citations[i]` : h
=> `l-i` : h 번 이상 인용된 논문의 개수

ex) `[0, 1, 3, 5, 6]`
=> `0 >= 5`, `1 >= 4`, **`3 >= 3`** => return 3

ex) `[0, 1, 5, 6]`
=> `0 >= 5`, `1 >= 4`, **`5 >= 2`** => return 2

![](https://images.velog.io/images/jsh5408/post/a82204bc-876c-4fc3-96e9-d7213bb67f17/image.png)

훨씬 빠르다