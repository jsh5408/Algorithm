from sys import stdin
import collections

x = [0]*3
y = [0]*3
a = 0
b = 0

for i in range(3):
    x[i], y[i] = map(int, stdin.readline().split())

xcnt = collections.Counter(x)
ycnt = collections.Counter(y)

for k, v in xcnt.items():
    if v == 1:
        a = k

for k, v in ycnt.items():
    if v == 1:
        b = k

print(a, b)