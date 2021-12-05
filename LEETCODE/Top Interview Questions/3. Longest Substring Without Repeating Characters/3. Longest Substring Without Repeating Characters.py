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