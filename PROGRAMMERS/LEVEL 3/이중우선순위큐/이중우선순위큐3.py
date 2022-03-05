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