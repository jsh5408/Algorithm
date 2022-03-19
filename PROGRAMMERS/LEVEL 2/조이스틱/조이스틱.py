def solution(name):
    answer = 0
    
    ### 위, 아래 개수 세기 ###
    for n in name:
        asc = ord(n) - ord("A")
        if asc > 13:
            asc = 13 - (asc % 13)
        answer += asc
    
    ### 왼, 오 개수 세기 ###
    ### A 가 없거나 뒤쪽에 있을 경우 => 오른쪽으로 가는게 가장 빠름
    idx = name.find("A")
    if idx == -1 or idx > len(name) // 2:
        answer += len(name) - 1
        return answer
        
    ### 왼쪽으로 가는 경우 확인
    path = len(name) - 1
    for i in range(1, len(name)):
        tmp = i-1
        if name[i] == "A":
            n = name[i:] + name[:i]
            while n[0] == "A":
                n = n[1:]
            tmp += len(n)-1
            path = min(path, tmp)
    
    answer += path
    
    return answer