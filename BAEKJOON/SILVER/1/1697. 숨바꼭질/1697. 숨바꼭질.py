import sys
sys.setrecursionlimit(10**5)

N, K = map(int, sys.stdin.readline().split())

ans = abs(K-N)
M = N
while M < K:
    M *= 2

def func(n, k, cnt):
    global ans, M
    
    if ans < cnt:
        return
    if n == k:
        ans = min(ans, cnt)
        return

    # 걷기
    if n-1 >= 0 and cnt+1 <= ans:
        func(n-1, k, cnt+1)
    if n+1 <= k and cnt+1 <= ans:
        func(n+1, k, cnt+1)

    # 순간이동
    if n*2 <= M and cnt+1 <= ans:
        func(n*2, k, cnt+1)

func(N, K, 0)
print(ans)
