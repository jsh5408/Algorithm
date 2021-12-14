## 9012. 괄호 - python3
https://www.acmicpc.net/problem/9012

#### 내 풀이 - 성공
```
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    s = stdin.readline().strip()
    stack = []
    ans = "YES"
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            if stack:
                stack.pop()
            else:
                ans = "NO"
                break
    if stack:
        ans = "NO"
    print(ans)
```
열린 괄호는 stack 에 저장하고
닫힌 괄호는 stack 에 값이 있으면 pop
stack 에 값이 없는데 닫힌 괄호가 들어왔거나 열린 괄호만 남을 경우 NO 출력

![](https://images.velog.io/images/jsh5408/post/26f3abd7-60b7-420e-b913-0846c092413a/image.png)