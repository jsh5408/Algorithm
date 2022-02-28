## 다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583

#### 내 아이디어
여러대의 트럭이 함께 가는 경우,
맨 앞의 트럭만 `len(truck_weights)` 만큼 걸리고
함께 가는 트럭들은 1 만큼 걸리는 점을 이용해서
트럭마다 걸리는 시간을 계산하려고 했으나 안됨...ㅎ

ex) `6 3 1 2` 같은 경우는 6 이 먼저 도착하고 나서야 2 가 올라갈 수 있음

너무 어렵게 생각한 듯...

#### 다른 사람의 풀이
```
def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    sec = 0
    
    while q:
        sec += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
                
    return sec
```
`q` 를 다리라고 생각하고 다리 길이만큼의 리스트 생성

while 문이 돌아가는 동안 `sec + 1` & `q.pop(0)`

현재 트럭이 다리 위에 올라가도 된다면 `q` 에 append
무게가 안된다면 0 append

반복문이 돌아가면서 실제로 트럭이 지나가듯이 `q` 가 변화함