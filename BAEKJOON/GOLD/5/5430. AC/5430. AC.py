from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    p = list(stdin.readline().strip())
    n = int(stdin.readline())
    arr = stdin.readline().strip()
    s = 0
    e = n-1
    flag = 1
    for rd in p:
        if rd == "R":
            flag = 0 if flag else 1
        else:
            n -= 1
            if n < 0:
                break
            if flag:
                s += 1
            else:
                e -= 1
    if n >= 0:
        arr = arr[1:-1]
        arr = arr.split(",")
        arr = arr[s:e+1]
        if flag == 0:
            arr.reverse()
        print("["+",".join(arr)+"]")
    else:
        print("error")