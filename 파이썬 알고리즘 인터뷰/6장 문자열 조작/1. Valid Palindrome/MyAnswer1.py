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