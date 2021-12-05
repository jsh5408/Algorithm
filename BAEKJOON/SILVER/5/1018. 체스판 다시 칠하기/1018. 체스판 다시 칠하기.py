N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        W = 0
        B = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        W += 1
                    if original[i][j] != 'B':
                        B += 1
                else:
                    if original[i][j] != 'B':
                        W += 1
                    if original[i][j] != 'W':
                        B += 1
        count.append(min(W, B))

print(min(count))