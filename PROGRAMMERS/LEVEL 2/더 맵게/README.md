## 더 맵게
https://programmers.co.kr/learn/courses/30/lessons/42626

#### 내 풀이
정확성: 76.2
효율성: 23.8
합계: 100.0 / 100.0
```
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b*2)
    
    return answer
```
`scoville` 을 heap 으로 바꿔줌 => min-heap 이용

가장 작은 값이 `K` 보다 커지면 모두 `K` 보다 큰 점을 이용
=> 스코빌 지수 최솟값이 `K` 보다 작을 동안
```
섞은 음식의 스코빌 지수
= 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
```
를 기반으로 최솟값 두개 pop 한 후 계산해서 push

스코빌이 하나만 남았을 경우는 섞을 수가 없으니까 return -1