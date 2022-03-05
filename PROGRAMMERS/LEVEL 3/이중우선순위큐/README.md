## 이중우선순위큐
https://programmers.co.kr/learn/courses/30/lessons/42628

#### 내 풀이 1
정확성: 100.0
합계: 100.0 / 100.0
```
import heapq

def solution(operations):
    heap = []

    for op in operations:
        op = op.split()
        if op[0] == "I":
            heap.append(int(op[1]))
        elif op[0] == "D" and heap:
            if op[1] == "1":
                heap.remove(max(heap))
            else:
                heap.remove(min(heap))
                
    if heap:
        return [max(heap), min(heap)]
    
    return [0, 0]
```
그냥 리스트로 append 하고 max, min 값 pop

#### 내 풀이 2
정확성: 83.3
합계: 83.3 / 100.0
```
import heapq

def solution(operations):
    heap = []

    for op in operations:
        op = op.split()
        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
        elif op[0] == "D" and heap:
            if op[1] == "1":
                heap.pop()
            else:
                heapq.heappop(heap)
                
    if heap:
        return [heap[-1], heap[0]]
    
    return [0, 0]
```
heap 이용

최댓값 return 할 때는 그냥 pop()
최솟값 return 할 때는 heappop()

근데.. 테스트케이스 하나가 통과되지 않음

이유 => **`heap[0]` 는 최솟값이라는 보장이 있지만 `heap[-1]` 이 최댓값이라는 보장이 없음!!!**

그럼 min-heap, max-heap 두가지를 써야할 듯

#### 내 풀이 3
정확성: 100.0
합계: 100.0 / 100.0
```
import heapq

def solution(operations):
    heap = []
    max_heap = []

    for op in operations:
        op = op.split()
        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
            heapq.heappush(max_heap, -int(op[1]))
        elif op[0] == "D" and heap:
            if op[1] == "1":
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
                heapq.heappop(max_heap)
            else:
                heapq.heappop(heap)
                max_heap = heapq.nlargest(len(max_heap), max_heap)[1:]
                heapq.heapify(max_heap)
                
    if heap:
        return [-max_heap[0], heap[0]]
    
    return [0, 0]
```
> **Min-Heap 에서 최댓값 없애는 방법**
```
heap = heapq.nlargest(len(heap), heap)[1:]
heapq.heapify(heap)
```
`nlargest(n, heap)` => 상위 n 개의 값만 가져옴
`[1:]` => 최댓값 하나만 지우는 slicing
`heapify` => 다시 heap 으로 만들어주기

를 참고해서 푼 풀이!!

min-heap, max-heap 두개 만들어서 똑같이 update 해준 후
마지막에 return 할 때 `max_heap` 은 마이너스를 붙여서 return