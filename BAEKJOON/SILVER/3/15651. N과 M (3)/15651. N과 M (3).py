from sys import stdin

N, M = map(int, stdin.readline().split())
nums = [i for i in range(1, N+1)]

def func(n, comb):
    if len(comb) == M:
        for c in comb:
            print(c, end=' ')
        print()
        return
    
    for i in range(len(n)):
        func(n, comb+[n[i]])

func(nums, [])