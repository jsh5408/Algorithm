# [프로그래머스/Level 3] 숫자 게임 - python3

**코딩테스트 연습 > Summer/Winter Coding(~2018) > 숫자 게임
**
https://programmers.co.kr/learn/courses/30/lessons/12987

---

#### 내 풀이
```
def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    i = 0
    for a in A:
        while i < len(B) and a >= B[i]:
            i += 1
        if i >= len(B):
            break
        else:
            answer += 1
            i += 1

    return answer
```

최종 스코어만 계산하면 되므로 순서는 상관이 없음
=> A, B 모두 정렬하고 비교

a 값을 기준으로 비교하면서 a 보다 큰 b 일 때만 answer + 1
나머지는 i += 1 하면서 큰 값을 찾아간다.

A, B 둘 중에 하나라도 다 확인했으면 break 해서 return

for 문 하나 & 투 포인터로 풀어도 된다

![](https://images.velog.io/images/jsh5408/post/1f8b0836-34b5-4a5e-af14-abbc1de0cdcf/image.png)
