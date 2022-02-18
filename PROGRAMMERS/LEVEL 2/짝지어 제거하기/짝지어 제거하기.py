import collections

def solution(s):
    # 1. 모든 문자가 짝수개인지 확인
    cnt = collections.Counter(s)
    
    for key, val in cnt.items():
        if val % 2 != 0:
            return 0
            
    # 2. 연속된 문자 제거
    stack = "0"
    for i in range(len(s)):
        if stack[-1] == s[i]:
            if len(stack) > 1:
                stack = stack[:len(stack)-1]
            else:
                stack = ""
        else:
            stack += s[i]
            
    if len(stack) != 1:
        return 0
    
    return 1