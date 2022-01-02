from sys import stdin

A, B = map(int, stdin.readline().split())

# 최대공약수
def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

# 최소공배수
def LCM(a, b):
    result = (a*b) // GCD(a, b)
    return result

print(GCD(A, B))
print(LCM(A, B))