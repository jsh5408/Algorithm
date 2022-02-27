def solution(priorities, location):
    ans = 1
    i = 0
    cnt = 0
    while priorities:
        if priorities[1:] and priorities[0] < max(priorities[1:]):
            p = priorities.pop(0)
            priorities.append(p)
            if location == 0:
                location = len(priorities)
        else:
            if location == 0:
                break
            priorities.pop(0)
            ans += 1
        location -= 1
        cnt += 1
    
    return ans