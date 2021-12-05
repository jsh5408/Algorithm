from sys import stdin

N, M = map(int, stdin.readline().split())
ans = [0] * (M)

nums = {}
names = {}
for i in range(N):
    inp = stdin.readline().strip()
    nums[i+1] = inp
    names[inp] = i+1

for i in range(M):
    Q = stdin.readline().strip()
    if Q.isdigit():
        print(nums[int(Q)])
    else:
        print(names[Q])