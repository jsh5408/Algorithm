def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    i = 0
    for a in A:
        while i < len(B) and a >= B[i]:
            i += 1
        if i >= len(B):
            break
        else:
            answer += 1
            i += 1

    return answer