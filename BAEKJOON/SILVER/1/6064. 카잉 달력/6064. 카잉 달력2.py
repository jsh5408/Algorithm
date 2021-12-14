from sys import stdin

T = int(stdin.readline())

for i in range(T):
    M, N, x, y = map(int, stdin.readline().split())
    ans = -1
    while(x <= M*N):
        if (x-y) % N == 0:	# if x % N == y % N:
            ans = x
            break
        x += M
    print(ans)