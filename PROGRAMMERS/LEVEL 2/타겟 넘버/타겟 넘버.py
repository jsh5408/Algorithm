def func(numbers, target, t):
    if len(numbers) == 0:
        if t == target:
            return 1
        return 0
    
    ans = 0
    ans += func(numbers[1:], target, t+numbers[0])
    ans += func(numbers[1:], target, t-numbers[0])
    
    return ans

def solution(numbers, target):
    answer = 0
    
    answer = func(numbers, target, 0)
    
    return answer