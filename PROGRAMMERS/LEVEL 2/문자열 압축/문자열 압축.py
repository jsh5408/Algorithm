def solution(s):
    answer = len(s)
    
    for j in range(len(s)):
        cnt = 1
        prev = s[:j+1]
        tmp = ""
        for i in range(j+1, len(s), j+1):
            if len(tmp) > answer:  # 최솟값을 구하는 것이므로 큰 값은 볼 필요가 X
                break
            if prev == s[i:i+j+1]: # 같으면 +1
                cnt += 1
            else:
                if cnt != 1:	# 1 은 생략하기 위해서
                    tmp += str(cnt)
                tmp += prev
                prev = s[i:i+j+1] # 지금 값으로 초기화
                cnt = 1		# 1 로 초기화
        # 마지막 값 처리
        if cnt != 1:
            tmp += str(cnt)
        tmp += prev
        
        # 최솟값으로 update
        if len(tmp) < answer:
            answer = len(tmp)
    
    return answer