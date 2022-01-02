from sys import stdin

N = int(stdin.readline())

arr = []
for i in range(N):
    a = list(map(int, stdin.readline().split()))
    arr.append(a)

arr.sort(key = lambda x:(x[1], x[0]))

ans = 0
end = 0
for s, e in arr:
    if end <= s or e < end:
        end = e
        ans += 1

print(ans)