## 전화번호 목록 - Level 2
https://programmers.co.kr/learn/courses/30/lessons/42577

#### 내 풀이 - 정확성: 83.3 | 효율성: 16.7 | 합계: 100.0 / 100.0
```
def solution(phone_book):
    phone_book.sort(key=len)
    prefix = set()
    for p in phone_book:
        for i in range(1, len(p)):
            if p[:i] in prefix:
                return False
        prefix.add(p)
    
    return True
```
길이 기준으로 정렬한 후

짧은 애들부터 `prefix` 에 넣어주면서
다음 번호들의 시작 값이 `prefix` 인지 확인