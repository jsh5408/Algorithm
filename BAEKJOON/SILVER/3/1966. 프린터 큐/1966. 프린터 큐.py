from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    q = list(map(int, stdin.readline().split()))
    nums = [i for i in range(N)]
    i = 0
    while i < N:
        if i+1 < N and q[i] < max(q[i+1:]):
            q.append(q.pop(i))
            nums.append(nums.pop(i))
        else:
            i += 1
            
    print(nums.index(M)+1)