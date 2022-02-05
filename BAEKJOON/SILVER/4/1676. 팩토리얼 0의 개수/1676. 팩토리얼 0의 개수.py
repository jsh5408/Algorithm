from sys import stdin

N = int(stdin.readline())
ans = 0

five = 5
while five <= N:
    for n in range(five, N+1, five):
        ans += 1
    five *= 5
print(ans)