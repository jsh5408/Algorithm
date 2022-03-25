visited = []

def func(dic, com, net):
    global visited
    
    if visited[com]:
        return
    
    visited[com] = 1
    
    for i in range(len(net)):
        if visited[net[i]] == 0:
            func(dic, net[i], dic[net[i]])

def solution(n, computers):
    global visited
    answer = 0
    
    visited = [0] * n
    dic = {i:[] for i in range(n)}
    
    for i in range(len(computers)):
        for j in range(i+1, len(computers[i])):
            if i != j and computers[i][j]:
                dic[i].append(j)
                dic[j].append(i)
    
    for i in range(n):
        if visited[i] == 0:
            func(dic, i, dic[i])
            answer += 1
    
    return answer