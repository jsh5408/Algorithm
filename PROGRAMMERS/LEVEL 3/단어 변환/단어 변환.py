def func(begin, target, words, cnt):
    if begin == target:
        return cnt
    
    if len(words) == 0:
        return 0
    
    ans = float('inf')
    for i in range(len(begin)):
        for j in range(len(words)):
            if begin[:i]+begin[i+1:] == words[j][:i]+words[j][i+1:]:
                ans = min(ans, func(words[j], target, words[:j]+words[j+1:], cnt+1))
    return ans

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    answer = func(begin, target, words, 0)
    
    if answer == float('inf'):
        return 0
    
    return answer