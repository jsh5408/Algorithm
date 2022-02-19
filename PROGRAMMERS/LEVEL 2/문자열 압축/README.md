**코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 문자열 압축**
https://programmers.co.kr/learn/courses/30/lessons/60057

---

#### My Answer
```
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
```
```
전체 예시: aabbaccc
```

1. `prev` 에 1 개, 2 개, ..., ~ 로 늘려가면서 문자열을 저장 => `s[:j+1]`
ex) `a` -> `aa` -> `aab` -> `aabb` -> ...

2. `prev` 다음 위치부터 `prev` 와 같은 길이의 문자들을 비교해서 개수 세기
ex) `j = 3` => `prev = aa` / `s[i:i+j+1] = bb` -> `ac` -> `cc`
==> `tmp = (1)aa(1)bb(1)ac(1)cc`

3. `answer` 는 최솟값으로 update