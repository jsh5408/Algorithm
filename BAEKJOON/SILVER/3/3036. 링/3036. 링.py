from sys import stdin

N = int(stdin.readline())
rings = list(map(int, stdin.readline().split()))

def gcd(a, b):
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

for i in range(1, N):
    g = gcd(rings[0], rings[i])
    A = rings[0]//g
    B = rings[i]//g
    print(str(A) + "/" + str(B))