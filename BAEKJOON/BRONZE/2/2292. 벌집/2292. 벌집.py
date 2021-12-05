from sys import stdin

N = int(stdin.readline())

r = 1
a = 6
while r < N:
    r += a
    a += 6

print(a // 6)