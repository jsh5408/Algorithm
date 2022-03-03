## 디스크 컨트롤러
https://programmers.co.kr/learn/courses/30/lessons/42627

#### 내 아이디어
매 초마다 요청할 수 있는 모든 디스크별 걸리는 시간을 계산해서 최솟값을 pick
시간 => `시점 + 소요시간` 으로 계산
작업 중인 디스크만 소요시간 -1, 나머지는 +1

ex) `[[0, 3], [1, 9], [2, 6]]`
0초) **3 (0 + 3)** -> 첫번째 디스크 pick
1초) **3 (1 + 2)** or 10 (1 + 9)
2초) **3 (2 + 1)** or 11 (2 + 9) or 8 (2 + 6)
3초) 12 (3 + 9) or **9 (3 + 6)** -> 세번째 디스크 pick

but 구현은 못했다...

#### 다른 사람의 풀이
정확성: 100.0
합계: 100.0 / 100.0
```
import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    
    return int(answer // len(jobs))
```
`if start < j[0] <= now:` => 요청할 수 있는 디스크들만 heap 에 push
걸리는 시간을 기준으로 정렬하기 위해 `[j[1], j[0]]` 로

`start ~ now` 범위만큼 디스크가 작업 중이라 생각

최솟값을 pop 해서 작업 처리
=> `start`, `now` update 하고 해당 디스크 소요시간 `answer` 에 더해주기

heap 이 비어있으면 요청시간이 오지 않았다는 것이므로 `now + 1`

마지막엔 평균 return