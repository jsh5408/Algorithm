from sys import stdin

N, K = map(int, stdin.readline().split())

def func(N):
    if N <= 1:
        return 1
    
    return N * func(N-1)

print(func(N) // (func(K) * func(N-K)))