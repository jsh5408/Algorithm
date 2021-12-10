## 344. Reverse String - python3
https://leetcode.com/problems/reverse-string/

---

#### My Answer 1: Accepted (Runtime: 196 ms - 78.17% / Memory Usage: 18.3 MB - 94.12%)
```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
```
reverse() 함수 사용

- 가장 Python 다운 방식
- Two-Pointer 보다 빠름

> **reverse**
리스트 => reverse()
문자열 => 슬라이싱 이용 `s[::-1]` / `s[:] = s[::-1]`
>
이 문제는 `O(1)` extra memory 이므로 `s[:] = s[::-1]` 사용

#### My Answer 2: Accepted (Runtime: 192 ms - 89.26% / Memory Usage: 18.3 MB - 94.12%)
```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
```
좌우대칭으로 교환

---

#### Solution 1: Accepted (Runtime: 204 ms - 47.90% / Memory Usage: 18.4 MB - 94.12%)
```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```
Two-Pointer