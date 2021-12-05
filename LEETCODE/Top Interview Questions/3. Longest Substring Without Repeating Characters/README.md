## 3. Longest Substring Without Repeating Characters - python3
https://leetcode.com/problems/longest-substring-without-repeating-characters/

#### My Answer 1: Accepted (Runtime: 404 ms - 17.05% / Memory Usage: 14.2 MB - 93.12%)
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        tmp = ""
        for i in range(len(s)):
            tmp = s[i]
            for j in range(i+1, len(s)):
                if s[j] in tmp:
                    ans = max(ans, len(tmp))
                    break
                tmp += s[j]
            ans = max(ans, len(tmp))
        return ans
```
`tmp` 에 보던 문자들을 쭉 넣어주고 겹치면 `ans` 에 최댓값 update & `tmp` 초기화

#### Solution 1: Accepted (Runtime: 60 ms - 78.76% / Memory Usage: 14.2 MB - 94.27%)
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
            
        cnt = 0
        start = -1
        
        for i in range(len(s)):
            if s[i] in dic and start < dic[s[i]]:
                start = dic[s[i]]
            dic[s[i]] = i
            cnt = max(cnt, i-start)
        
        return cnt
```
저번에 풀었던 방식...^^

`dic` 에 가장 최신 인덱스 값을 넣어줌

중복이 없으면 `cnt` = 처음부터 지금 인덱스까지의 길이
중복을 만나면 `start` 는 이전 중복값의 위치 인덱스로 설정해서
중복과 중복 사이의 길이를 `cnt` 에 update
