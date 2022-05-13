from collections import Counter

def solution(participant, completion):
    pCnt = Counter(participant)
    cCnt = Counter(completion)
    for p, v in pCnt.items():
        if p not in cCnt or cCnt[p] != v:
            return p