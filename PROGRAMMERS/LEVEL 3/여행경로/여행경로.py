def func(dic, now, path, length):
    if length == 0:
        return [path]
    
    if len(dic[now]) == 0:
        return []
    
    ans = []
    for i in range(len(dic[now])):
        p = dic[now].pop(0)
        ans += func(dic, p, path+[p], length-1)
        dic[now].append(p)
    return ans

def solution(tickets):
    answer = []
    dic = {}
    
    for a, b in tickets:
        if a in dic:
            dic[a].append(b)
        else:
            dic[a] = [b]
        if b not in dic:
            dic[b] = []
    
    answer = func(dic, "ICN", ["ICN"], len(tickets))
    answer.sort()
    
    return answer[0]