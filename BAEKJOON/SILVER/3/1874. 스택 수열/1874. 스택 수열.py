n = int(input())
stack = [1]
inp = []
out = []
result = ["+"]

for _ in range(n):
    inp.append(int(input()))

i = 2
while inp:
    if len(stack) == 0 or inp[0] > stack[-1]:
        result.append("+")
        stack.append(i)
        i += 1
    elif inp[0] == stack[-1]:
        inp.pop(0)
        result.append("-")
        stack.pop()
    else:
        if inp[0] in out:
            break
        while stack and inp[0] != stack[-1]:
            result.append("-")
            out.append(stack.pop())

if len(inp) > 0:
    print("NO")
else:
    for r in result:
        print(r)