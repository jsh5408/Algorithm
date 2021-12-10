import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9a-zA-Z]', '', s)   # 공백, 특수문자 제거
        s = s.upper()
            
        return s == s[::-1]