## 819. Most Common Word
https://leetcode.com/problems/most-common-word/

---

#### My Answer 1: Accepted (Runtime: 48 ms - 20.71% / Memory Usage: 14.3 MB - 74.56%)
```
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace("'", " ")
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.lower()
        p = paragraph.split()
        
        for i in range(len(banned)):
            while banned[i] in p:
                p.remove(banned[i])
        
        dic = collections.defaultdict(int)
        for w in p:
            dic[w] += 1
        
        for k, v in dic.items():
            if v == max(dic.values()):
                return k
```
특수문자들 replace & 모두 소문자로 변경 & 공백 기준으로 split

`banned` 에 포함된 애들을 모두 remove

`dic` 에 단어 개수 저장해주고 가장 많이 나온 단어 return

> **replace**
여러개를 replace 하려면 replace() 를 여러번 사용해야 함
>
**re**
정규식 이용
>
```
import re
s = re.sub("[^\w]", " ", s)
```
* `\w` => 단어 문자 / `^` => not
=> 단어 문자가 아닌 모든 문자

> **Dictionary: 최댓값 value 에 해당하는 key 값 가져오기**
```
max(dic, key=dic.get)
```
`max(dic)`: 최대 key 값
`key = dic.get`: value 값을 기준으로
>
---
>
```
[k for k, v in dic.items() if max(dic.values()) == v]
```
items() 를 이용해서 최댓값 찾기

* banned 값 remove 대신 조건문 적용해서 count 안하기도 가능
* defaultdict 대신 Counter 이용해도 됨

---

#### Solution 1: Accepted (Runtime: 36 ms - 70.73% / Memory Usage: 14.5 MB - 21.20%)
```
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
                 if word not in banned]
        
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
```
re.sub 와 Counter 이용
> 
`counts.most_common(n)[i][0]`
=> `(k, v)` 튜플로 구성된 상위 n 개의 빈도수 리스트 중
i 번째 튜플의 key 값 가져오기