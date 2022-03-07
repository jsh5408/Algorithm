def solution(citations):
    answer = 0
    citations.sort()
    idx = 0
    
    for i in range(1, max(citations)):
        while idx < len(citations) and citations[idx] < i:
            idx += 1
        if idx <= i and len(citations) - idx >= i:
            answer = max(answer, i)
    
    return answer