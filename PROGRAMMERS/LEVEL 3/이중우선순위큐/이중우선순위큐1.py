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