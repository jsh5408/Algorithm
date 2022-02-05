M, N = map(int, input().split())
nums = [1]*(N+1)
nums[0], nums[1] = 0, 0

r = int(N**0.5)
for i in range(2, r+1):
    if nums[i]:
        for j in range(i+i, N+1, i):
            nums[j] = 0

for i in range(M, N+1):
    if nums[i]:
        print(i)