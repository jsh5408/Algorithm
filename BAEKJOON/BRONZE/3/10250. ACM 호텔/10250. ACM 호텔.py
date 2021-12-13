from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    H, W, N = map(int, stdin.readline().split())
    YY = N % H
    ans = ""
    if YY == 0:
        ans += str(H)
        XX = N // H
    else:
        ans += str(YY)
        XX = N // H + 1
    if XX < 10:
        ans += "0" + str(XX)
    else:
        ans += str(XX)
    print(ans)