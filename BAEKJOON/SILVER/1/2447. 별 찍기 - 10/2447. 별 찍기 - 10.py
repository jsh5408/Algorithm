from sys import stdin

N = int(stdin.readline())

arr = [["*"]*N for i in range(N)]

def func(si, sj, ei, ej, n):
    if si == ei or sj == ej:
        return

    tmp = n // 3
    
    for i in range(tmp):
        for j in range(tmp):
            arr[si+tmp+i][sj+tmp+j] = " "
    
    if n != 1:
        func(si, sj, si+tmp, sj+tmp, tmp)
        func(si+tmp, sj, si+tmp*2, sj+tmp, tmp)
        func(si+tmp*2, sj, ei, sj+tmp, tmp)
        
        func(si, sj+tmp, si+tmp, sj+tmp*2, tmp)
        func(si+tmp*2, sj+tmp, ei, sj+tmp*2, tmp)
        
        func(si, sj+tmp*2, si+tmp, ej, tmp)
        func(si+tmp, sj+tmp*2, si+tmp*2, ej, tmp)
        func(si+tmp*2, sj+tmp*2, ei, ej, tmp)

func(0, 0, N, N, N)

for i in range(N):
    for j in range(N):
        print(arr[i][j] ,end='')
    print()