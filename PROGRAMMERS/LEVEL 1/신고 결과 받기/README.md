## 신고 결과 받기
https://programmers.co.kr/learn/courses/30/lessons/92334

#### Dictionary - 성공
```
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
```
ids = 아이디별 신고 횟수 count
dic = 아이디별 신고자 저장
ans = 아이디별 신고 메일 수신 횟수

세개의 dic 를 사용했다

다른 풀이는
2차원 배열을 만들어서 A->B 신고를 arr[A][B] = 1 형태로 저장
각 행마다 1 의 개수를 세서 k 이상이면 1 인 값들에게 메일 전송
=> 행, 열 이용