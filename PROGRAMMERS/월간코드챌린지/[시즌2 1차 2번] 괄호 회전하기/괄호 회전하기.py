def solution(s):
    answer = 0
    
    for j in range(len(s)):
        s2 = s[j:] + s[:j]
        right = 0
        stack = []
        for i in range(len(s2)):
            if s2[i] == "(" or s2[i] == "[" or s2[i] == "{":
                stack.append(s2[i])
            else:
                if len(stack) == 0:
                    right = 0
                    break
                else:
                    if (s2[i] == ")" and stack[-1] == "(") or (s2[i] == "]" and stack[-1] == "[") or (s2[i] == "}" and stack[-1] == "{"):
                        right = 1
                        stack.pop()
                    else:
                        right = 0
                        break
        if right == 1 and len(stack) == 0:
            answer += 1
    
    return answer