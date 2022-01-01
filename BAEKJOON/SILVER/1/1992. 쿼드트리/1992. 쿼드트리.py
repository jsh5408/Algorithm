import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())

mat = []

for i in range(N):
    s = sys.stdin.readline().strip()
    tmp = []
    for c in s:
        tmp.append(int(c))
    mat.append(tmp)

def func(si, sj, ei, ej, n):
    val = mat[si][sj]
    flag = 1

    for i in range(si, ei):
        for j in range(sj, ej):
            if mat[i][j] != val:
                flag = 0
                break
    
    if flag == 1:
        return str(val)
    else:
        # 4등분
        s = "("
        if n//2 > 0:
            s += func(si, sj, si+n//2, sj+n//2, n//2) # 왼위
            s += func(si, sj+n//2, si+n//2, ej, n//2) # 오위
            s += func(si+n//2, sj, ei, sj+n//2, n//2) # 왼아
            s += func(si+n//2, sj+n//2, ei, ej, n//2) # 오아
        return s + ")"

ans = func(0, 0, N, N, N)
print(ans)