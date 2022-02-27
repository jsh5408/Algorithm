## 프린터
https://programmers.co.kr/learn/courses/30/lessons/42587

#### 내 풀이
정확성: 100.0
합계: 100.0 / 100.0
```
def solution(priorities, location):
    ans = 1
    i = 0
    cnt = 0
    while priorities:
        if priorities[1:] and priorities[0] < max(priorities[1:]):
            p = priorities.pop(0)
            priorities.append(p)
            if location == 0:
                location = len(priorities)
        else:
            if location == 0:
                break
            priorities.pop(0)
            ans += 1
        location -= 1
        cnt += 1
    
    return ans
```
`priorities` 의 첫번째 값만 보면서 이후에 더 큰 값이 있으면 맨 뒤로 붙여줌
=> pop(0) & append(p)
이 때, `location` 에 해당되는 문서였으면 맨 뒤로 갔으니까
`location = len(priorities)` 로 update

이후에 더 큰 값이 없다면 출력 확정이니까 pop(0) & 출력 횟수 (`ans`) + 1
이 때, `location` 이 확정되는 거면 이후는 볼 필요가 없으니까 break

#### 다른 사람의 풀이
정확성: 100.0
합계: 100.0 / 100.0
```
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
```
`queue` 에 (인덱스, 우선순위) 로 묶어서 저장

처음 값을 pop 한 후 남은 `queue` 의 우선순위들 중에 더 높은게 있는지 확인
* `any()`: 하나라도 True 가 있는지 확인

있으면 다시 `queue` 에 append
없으면 `answer + 1` 하고 `location` 인지 확인