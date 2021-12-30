from sys import stdin

T = int(stdin.readline())

dp = []

for i in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())

    nums = [i for i in range(n+1)]
    ans = 0
    for _ in range(k):
        for j in range(1, n+1):
            nums[j] += nums[j-1]
    
    print(nums[-1])