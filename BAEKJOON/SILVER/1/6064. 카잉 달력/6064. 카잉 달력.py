from sys import stdin

T = int(stdin.readline())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(T):
    M, N, x, y = map(int, stdin.readline().split())
    a, b = x, y
    lcm = M*N // gcd(M, N)
    while a != b:
        if a < b:
            a += M
        else:
            b += N
        if a > lcm or b > lcm:
            a = -1
            break
    print(a)