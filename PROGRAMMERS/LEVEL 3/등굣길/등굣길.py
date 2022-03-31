def solution(m, n, puddles):
    mapp = [[0] * (m+1) for _ in range(n+1)]
    
    mapp[1][1] = 1
    
    for x in range(1, n+1):
        for y in range(1, m+1):
            if x == 1 and y == 1:
                continue
                
            if [y, x] in puddles:
                mapp[x][y] = 0
            else:
                mapp[x][y] = mapp[x-1][y] + mapp[x][y-1]
    
    return mapp[-1][-1] % 1000000007