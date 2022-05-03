from sys import stdin

N, K = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

tmp = sum(nums[:K])
ans = tmp

for i in range(K, N):
    tmp += nums[i] - nums[i-K]
    ans = max(ans, tmp)

print(ans)