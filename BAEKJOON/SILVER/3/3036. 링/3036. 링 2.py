from sys import stdin

N = int(stdin.readline())
rings = list(map(int, stdin.readline().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(1, N):
    g = gcd(rings[0], rings[i])
    A = rings[0]//g
    B = rings[i]//g
    print(str(A) + "/" + str(B))