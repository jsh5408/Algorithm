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