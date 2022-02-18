**코딩테스트 연습 > 2017 팁스타운 > 짝지어 제거하기**
https://programmers.co.kr/learn/courses/30/lessons/12973

---

#### My Answer
```
import collections

def solution(s):
    # 1. 모든 문자가 짝수개인지 확인
    cnt = collections.Counter(s)
    
    for key, val in cnt.items():
        if val % 2 != 0:
            return 0
            
    # 2. 연속된 문자 제거
    stack = "0"
    for i in range(len(s)):
        if stack[-1] == s[i]:
            if len(stack) > 1:
                stack = stack[:len(stack)-1]
            else:
                stack = ""
        else:
            stack += s[i]
            
    if len(stack) != 1:
        return 0
    
    return 1
```
1. 모든 문자가 짝수개인지 확인
Counter 를 이용해서 value 값이 짝수인지 확인

2. 연속된 문자 제거
`stack` 문자열에 `0` 만 미리 넣어두고 (=> 문자열 길이 신경쓰기 싫어서..)
반복문 돌려서 `stack` 의 맨 끝 값과 `s[i]` 값이 같은지 확인

 다르면 `stack` 에 `s[i]` 값 넣어주기
 같으면 같은 문자만 `stack` 에서 빼줌

3. 마지막에 `0` 만 남지 않으면 제거되지 않은 것이므로 `return 0`

4. 나머지는 `return 1`