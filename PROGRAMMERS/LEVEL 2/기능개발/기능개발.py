def solution(progresses, speeds):
    ans = []
    release = []
    for i in range(len(progresses)):
        p = (100 - progresses[i])
        r = p // speeds[i]
        if p % speeds[i] != 0:
            r += 1
        release.append(r)
    
    prev = release[0]
    cnt = 0
    for r in release:
        if prev < r:
            ans.append(cnt)
            prev = r
            cnt = 1
        else:
            cnt += 1
    ans.append(cnt)
    
    return ans