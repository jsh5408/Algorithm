## 937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/

---

#### My Answer 1: Accepted (Runtime: 32 ms - 90.43% / Memory Usage: 14.5 MB - 37.42%)
```
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for i in range(len(logs)):
            log = logs[i].split()
            if log[1].isdigit():
                digits.append(logs[i])
            else:
                letters.append(logs[i])
        
        letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        
        return letters + digits
```
split() 한 후 `[1]` 번째 값이 digit 인지 확인해서
`letters` 와 `digits` 구분

`letters` 는 contents 기준 (1) & identifier 기준 (2) 으로 정렬

> **람다 표현식**
: 식별자 없이 실행 가능한 함수
>
ex)
```
s.sort(key=lambda x:(x.split()[1:], x.split()[0]))
```
---
>
```
def func(x):
    return x.split()[1:], x.split()[0]
s.sort(key=func)
```
처럼 함수를 `key` 값으로 사용해도 가능
>
* 가독성 주의