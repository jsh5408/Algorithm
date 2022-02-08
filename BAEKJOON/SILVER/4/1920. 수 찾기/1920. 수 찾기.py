N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for b in B:
    TF = 0
    l = 0
    r = N-1
    while l <= r:
        m = (l+r) // 2
        if A[m] == b:
            TF = 1
            break
        if A[m] < b:
            l = m+1
        else:
            r = m-1
    if TF:
        print(1)
    else:
        print(0)