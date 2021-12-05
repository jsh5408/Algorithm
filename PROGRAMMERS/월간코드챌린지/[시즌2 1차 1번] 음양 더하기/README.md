# [Review] 월간 코드 챌린지 시즌2 1차 1번 - 음양 더하기 - python3

#### 음양 더하기 - Level 1
https://programmers.co.kr/learn/courses/30/lessons/76501

---

#### My Answer
```
def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer
```

`sign` 값이 `True` 면 더해주고 `False` 면 빼주기

---

> **for 문에서 zip() 사용**
=> 지금 문제처럼 여러 개의 리스트에서 같은 인덱스의 값을 가져올 때 사용
ex) `(4, True)`, `(7, False)`
