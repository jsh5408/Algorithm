https://programmers.co.kr/learn/courses/30/lessons/42576

#### Dictionary - 성공
```
from collections import Counter

def solution(participant, completion):
    pCnt = Counter(participant)
    cCnt = Counter(completion)
    for p, v in pCnt.items():
        if p not in cCnt or cCnt[p] != v:
            return p
```
참가자 이름별 숫자와 완주자 이름별 숫자를 Counter 로 구함
두 값을 비교하며 완주자가 아니거나 같은 이름의 완주한 사람 수와 참가한 사람 수가 다르면 return

![](https://velog.velcdn.com/images/jsh5408/post/b12110ee-229d-4e78-9107-732cc547e644/image.png)
