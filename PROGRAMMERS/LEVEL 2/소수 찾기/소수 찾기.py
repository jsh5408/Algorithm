combinations = set()
def solution(numbers):
    global combinations
    def comb(nums, c):
        if c and int(c) > 1:
            combinations.add(int(c))
        
        if len(nums) == 0:
            return
        
        for i in range(len(nums)):
            comb(nums[:i] + nums[i+1:], c+nums[i])
    
    comb(numbers, "")
    
    answer = 0
    for c in combinations:
        isPrime = 1
        for i in range(2, int(c**0.5)+1):
            if c % i == 0:
                isPrime = 0
                break
        if isPrime:
            answer += 1
    
    return answer