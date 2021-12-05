N = int(input())
M = int(input())
enable = {str(i) for i in range(10)}

# 고장난 버튼 제거
if M != 0:
    enable -= set(map(str, input().split()))

ans = abs(100 - N)

for n in range(1000001):
    n = str(n)
    for j in range(len(n)):
        if n[j] not in enable:
            break
        elif j == len(n) - 1:
            ans = min(ans, abs(N - int(n)) + len(str(n)))
print(ans)