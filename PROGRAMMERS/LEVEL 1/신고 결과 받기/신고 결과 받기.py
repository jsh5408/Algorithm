import collections

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    ids = collections.defaultdict(int)
    dic = collections.defaultdict(list)
    ans = collections.defaultdict(int)
    
    for i in range(len(report)):
        A, B = map(str, report[i].split())
        if A not in dic[B]:
            dic[B].append(A)
            ids[B] += 1
    
    for key, v in ids.items():
        if v >= k:
            for i in dic[key]:
                ans[i] += 1
    
    for i in range(len(id_list)):
        answer[i] = ans[id_list[i]]
    
    return answer