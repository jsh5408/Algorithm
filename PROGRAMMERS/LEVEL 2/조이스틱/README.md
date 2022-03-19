## 조이스틱
https://programmers.co.kr/learn/courses/30/lessons/42860

#### 내 풀이 - 통과
```
def solution(name):
    answer = 0
    
    ### 위, 아래 개수 세기 ###
    for n in name:
        asc = ord(n) - ord("A")
        if asc > 13:
            asc = 13 - (asc % 13)
        answer += asc
    
    ### 왼, 오 개수 세기 ###
    ### A 가 없거나 뒤쪽에 있을 경우 => 오른쪽으로 가는게 가장 빠름
    idx = name.find("A")
    if idx == -1 or idx > len(name) // 2:
        answer += len(name) - 1
        return answer
        
    ### 왼쪽으로 가는 경우 확인
    path = len(name) - 1
    for i in range(1, len(name)):
        tmp = i-1
        if name[i] == "A":
            n = name[i:] + name[:i]
            while n[0] == "A":
                n = n[1:]
            tmp += len(n)-1
            path = min(path, tmp)
    
    answer += path
    
    return answer
```
1. 위, 아래로 움직일 때의 횟수 세기
`A ~ M` 까지는 위로, `N ~ Z` 까지는 아래로 움직이는게 최솟값이므로
절반인 13 을 기준으로 횟수 계산해줌

2. 왼, 오 횟수 세기 - 오른쪽으로 쭉 가는 경우
`A` 가 아예 없거나 뒤쪽에 있는 경우는 그냥 오른쪽으로 한칸씩 움직이는게 가장 짧음
=> `len(name) - 1` 더해서 return

3. 왼쪽으로 가는 경우 == `A` 가 절반 앞쪽에 있는 경우
`path` 는 오른쪽으로 쭉 가는 경우로 초기화
0 자리에는 어떤 값이 있든 움직일 필요가 없으므로 1 부터 시작
`A` 를 만나면 슬라이싱으로 `A` 까지의 값들을 맨 뒤로 보내고 앞의 `A` 들을 모두 제거
ex) `"JEAAN"` => `"AANJE"` => `"NJE"`
=> 왼쪽은 `i-1` 번 움직이고 오른쪽으로 `len(n)-1` 번 움직임
=> 둘을 더해서 최솟값만 `answer` 에 추가

깔끔하지는 못하다...ㅎ

![](https://images.velog.io/images/jsh5408/post/c1029a30-c33d-4d19-98ce-ae704bb3b236/image.png)

#### 다른 사람의 풀이
```
def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer
```
이것도 우선 위, 아래의 경우 처리
=> alphabet_to_num 함수로 `A ~ M` 는 `0 ~ 12`, `N ~ Z` 는 `1 ~ 13` 의 값을 갖게 함

현재 숫자 바로 다음에 몇개의 `A` 가 연속되어있는지 개수를 세줌
그러면 `idx` 와 `next_idx` 를 기준으로 세 그룹으로 나뉜다
=> **`0 ~ idx` & `A 무리들` & `next_idx ~ 끝`**

`distance` : 1그룹 (`idx`) 과 2그룹 (`n - next_idx`) 중에 더 작은 값을 찾음
=> 왼 -> 오 or 오 -> 왼 처럼 **겹치는 부분**이 된다

총 움직인 횟수 `move` 는
중간 `A` 들을 제외한 **1그룹과 2그룹의 이동 횟수 + 겹치는 부분 `distance`** 가 됨


![](https://images.velog.io/images/jsh5408/post/b208680e-da46-44ee-ac7d-e36c2b8d4c42/image.png)