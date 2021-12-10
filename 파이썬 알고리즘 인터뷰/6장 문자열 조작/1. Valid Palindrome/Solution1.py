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