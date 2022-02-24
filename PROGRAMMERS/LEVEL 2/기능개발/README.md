## 기능개발
https://programmers.co.kr/learn/courses/30/lessons/42586

#### 내 풀이
정확성: 100.0
합계: 100.0 / 100.0
```
def solution(progresses, speeds):
    ans = []
    release = []
    for i in range(len(progresses)):
        p = (100 - progresses[i])
        r = p // speeds[i]
        if p % speeds[i] != 0:
            r += 1
        release.append(r)
    
    prev = release[0]
    cnt = 0
    for r in release:
        if prev < r:
            ans.append(cnt)
            prev = r
            cnt = 1
        else:
            cnt += 1
    ans.append(cnt)
    
    return ans
```
잔여 업무를 속도로 나눈 값 = 배포까지 걸리는 시간을 `release` 에 저장

`release` 를 보면서 이전 값보다 큰 값이 나오면 그 사이 개수를 `ans` 에 저장
작은 값들은 `cnt + 1` 로 카운트