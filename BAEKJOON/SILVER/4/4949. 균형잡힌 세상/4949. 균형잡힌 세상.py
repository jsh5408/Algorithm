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