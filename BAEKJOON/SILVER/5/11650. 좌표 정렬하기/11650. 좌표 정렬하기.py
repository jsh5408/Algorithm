from sys import stdin

N = int(stdin.readline())
coords = []

for _ in range(N):
    x, y = map(int, stdin.readline().split())
    coords.append((x, y))

coords.sort(key = lambda x: (x[0], x[1]))

for x, y in coords:
    print(x, y)