#### 괄호 회전하기 - Level 2
https://programmers.co.kr/learn/courses/30/lessons/76502

---

#### My Answer
```
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
```

첫번째 반복문 => `s` 를 1 칸씩 rotate
두번째 반복문 => 여는 괄호면 `stack` 에 넣어주고 닫는 괄호면 `stack[-1]` 값이랑 짝꿍인지 확인
짝꿍이면 `right = 1` 다르면 `right = 0`
`stack` 이 비어있는데 닫는 괄호부터 만나도 마찬가지로 `right = 0`

최종적으로 `right == 1 and len(stack) == 0` 이면 `answer += 1`