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