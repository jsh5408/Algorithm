K, N = map(int, input().split())
lines = []
ans = 0

for _ in range(K):
    lines.append(int(input()))

left = 1
right = max(lines)

while left <= right:
    mid = (left+right) // 2

    cnt = 0
    for l in lines:
        cnt += l // mid
    if cnt >= N:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)