from sys import stdin

T = int(stdin.readline())

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
        
    return num

for i in range(T):
    N, M = map(int, stdin.readline().split())
    ans = factorial(M) // (factorial(N) * factorial(M - N))
    print(ans)