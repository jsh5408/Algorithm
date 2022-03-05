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