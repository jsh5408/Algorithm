from sys import stdin

N, M = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))

cards.sort()

ans = 0

for a in range(len(cards)-1, 1, -1):
    for b in range(a-1, 0, -1):
        tmp = cards[a]
        if tmp + cards[b] < M:
            tmp += cards[b]
            for c in range(b-1, -1, -1):
                if tmp + cards[c] <= M:
                    ans = max(ans, tmp+cards[c])
                    break
        if ans == M:
            break
    if ans == M:
        break

print(ans)