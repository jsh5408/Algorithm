**<참고>**
문자열에서 `a = b` 는 참조 / `a[:] = b` 는 복사

---

## 125. Valid Palindrome - python3
https://leetcode.com/problems/valid-palindrome/

---

#### My Answer 1: Accepted (Runtime: 56 ms - 32.06% / Memory Usage: 14.6 MB - 62.39%)
```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                clear += s[i].lower()
        
        for i in range(0, len(clear)//2):
            if clear[i] != clear[len(clear)-i-1]:
                return False
        
        return True
```
문자, 숫자만 `clear` 에 넣어주고
처음과 끝부터 대칭으로 비교하면서 다르면 `return False`, 모두 같으면 `return True`

> `isalpha()` => 영어/한글 문자인지 판단해서 T/F 반환
`isdigit()` => 숫자인지 판단해서 T/F 반환
`isalnum()` => 영어/한글/숫자인지 판단해서 T/F 반환

* `clear` 가 string 일 때보다 list 가 더 느림
* list 는 인덱스로 비교하는 것보다 `pop` 해서 비교하는게 더 느림

---

#### Solution 1: Accepted (Runtime: 48 ms - 63.41% / Memory Usage: 19.4 MB - 15.55%)
```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear = collections.deque()
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                clear.append(s[i].lower())
        
        while len(clear) > 1:
            if clear.popleft() != clear.pop():
                return False
        
        return True
```
deque 를 이용해서 `popleft()` 와 `pop()` 비교하기

* list 보다 훨씬 빠름 (list: 260 ms / deque: 48 ms)
* `n` 번 반복 시, deque 는 `O(n)` / list 는 `O(n^2)`
> `popleft()` => `O(1)` / `pop()` => `O(n)`

#### Solution 2: Accepted (Runtime: 52 ms - 47.18% / Memory Usage: 15.4 MB - 28.32%)
```
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9a-zA-Z]', '', s)   # 공백, 특수문자 제거
        s = s.upper()
            
        return s == s[::-1]
```
공백, 특수문자 제거 후, 슬라이싱으로 같은지 비교

* 더 짧고, 빠르다.

> 문자열은 슬라이싱을 우선으로 => 속도 Good