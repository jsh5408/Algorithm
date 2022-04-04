## 입국심사
https://programmers.co.kr/learn/courses/30/lessons/43238

#### 내 아이디어
각 심사관들의 배수들을 모두 저장해서 `n` 번째 값 return

ex) `n = 6 | times = [7, 10] | return = 28`
7 의 배수 => `[7, 14, 21, 28, 35, ...]`
10 의 배수 => `[10, 20, 30, 40, ...]`
모두 합치면 `[7, 10, 14, 20, 21, 28, 30, ...]`
=> 7 분에 끝나는 것 하나, 10 분에 끝나는 것 하나, 14 분에 끝나는 것 하나, ...
`n` 번째는 28 분에 끝남

하지만 범위가 너무 크고... 배수의 제한을 잡기 힘듦...

> 제한사항
* 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
* 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
* 심사관은 1명 이상 100,000명 이하입니다.

#### 다른 사람의 풀이
```
def solution(n, times):
    answer = 0
    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            end = mid
        else:
            start = mid + 1
            
    answer = start
    
    return answer
```
`start` : 최소 1 분
`end` : 최대 `times[-1] * n` 분

로 잡고 이분탐색을 돌리기

`total` : 몇명의 인원을 심사할 수 있는지 세줌

ex) `n = 6 | times = [7, 10] | return = 28`
`start = 1` `mid = 30` `end = 60` => 7 명 & `end` 변경
`start = 1` `mid = 15` `end = 30` => 3 명 & `start` 변경
`start = 15` `mid = 27` `end = 30` => 5 명 & `start` 변경
`start = 27` `mid = 28` `end = 30` => 6 명 & `end` 변경
`start = 27` `mid = 27` `end = 28` => 5 명 & `start` 변경
`start = 28` `mid = 28` `end = 28` => return 28

인덱스에 대한 이분탐색만 봐왔는데 값으로도 가능한게 신기했다

![](https://images.velog.io/images/jsh5408/post/e88c280a-215e-473c-833e-5c19f6dc169b/image.png)