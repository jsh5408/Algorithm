inp = input().split("-")
ans = 0

first = inp.pop(0).split("+")
for n in first:
    ans += int(n)

for i in inp:
    tmp = 0
    nums = i.split("+")
    for n in nums:
        tmp += int(n)
    ans -= tmp

print(ans)