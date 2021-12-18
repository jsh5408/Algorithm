## 4949. 균형잡힌 세상 - python3
https://www.acmicpc.net/problem/4949

#### 내 풀이 - 성공
```
from sys import stdin

while True:
    s = stdin.readline().rstrip()
    if s == ".":
        break
    ans = 1
    stack = []
    for ch in s:
        if ch == "(" or ch == ")" or ch == "[" or ch == "]":
            if ch == "(" or ch == "[":
                stack.append(ch)
            elif stack and ch == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and ch == "]" and stack[-1] == "[":
                stack.pop()
            else:
                ans = 0
                break
    if ans and len(stack) == 0:
        print("yes")
    else:
        print("no")
```
입력받은 문자열은 오른쪽 끝만 strip() 해주기

"." 이면 종료 설정

나머지는 stack 을 이용해서 괄호가 올바른지 확인
여는 괄호면 append
닫는 괄호면 stack 의 top 값과 매치되는지 확인해서 pop
매치되지 않거나 남은 괄호가 있다면 no 출력

![](https://images.velog.io/images/jsh5408/post/039969dc-86a6-452b-9a61-8d2c497b384c/image.png)