from sys import stdin

N = int(stdin.readline())
nums = [-1]*(N+1)

if N == 3:
    print(1)
elif N == 4:
    print(-1)
else:
    nums[3] = 1
    nums[5] = 1

    for i in range(6, N+1):
        if nums[i-5] != -1:
            nums[i] = nums[5] + nums[i-5]
        elif nums[i-3] != -1:
            nums[i] = nums[3] + nums[i-3]
    print(nums[N])