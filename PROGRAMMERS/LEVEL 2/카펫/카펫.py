def solution(brown, yellow):
    answer = []
    
    for i in range(yellow, 0, -1):
        w = i
        h = yellow // i + yellow % i
        b = w * 2 + h * 2 + 4 + (w*h - yellow)
        if b == brown:
            if w > h:
                return [w+2, h+2]
            else:
                return [h+2, w+2]
    
    return answer