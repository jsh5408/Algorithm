from sys import stdin

T = int(stdin.readline())

def func(a, b):
    while b:
        a, b = b, a%b
    return a

for i in range(T):
    A, B = map(int, stdin.readline().split())
    gcd = func(A, B)
    print(A * B // gcd)