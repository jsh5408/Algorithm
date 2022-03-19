## 큰 수 만들기
https://programmers.co.kr/learn/courses/30/lessons/42883

#### 내 풀이 1 - 실패
```
from itertools import combinations

def solution(number, k):
    p = max(list(map("".join, combinations(number, len(number)-k))))
    return p
```
combinations 함수로 `len(number)-k` 길이의 모든 조합을 구한 후, 최댓값 return

참고로 직접 재귀 함수를 만들어서 해도 타임리밋,,

![](https://images.velog.io/images/jsh5408/post/469e41fb-0988-474e-8671-4b4c09893eb5/image.png)

#### 내 풀이 2 - 실패
```
def solution(number, k):
    answer = "0"
    k += 1
    prev = "0"
    for i in range(len(number)):
        if prev <= number[i]:
            for j in range(len(answer)):
                if answer[j] >= number[i]:
                    break
            if j < k:
                answer = answer[j:]
                k -= j
            else:
                answer = answer[k:]
                k = 0
            answer += number[i]
        elif prev > number[i]:
            k -= 1
        if k == 0:
            answer += number[i+1:]
            break
        prev = number[i]
            
    return answer
```
그래서 조합을 모두 찾는 것 말고
이전 값보다 큰 숫자들이 나올 때마다 그 이전의 값들은 없애주는 방식을 생각

`answer` 에 임의로 0 을 추가, 이 0 도 제거돼야 하므로 `k += 1`

`prev` 와 비교해서 큰 숫자를 만나면 `answer` 에 있는 숫자들 중 작은 값들은 `k` 개 만큼 삭제
삭제할 개수와 `k` 를 비교해서 0 이 되는지 범위 체크

했지만 실패!!
너무 끼워맞추듯이 하다보니 지저분해졌다...

![](https://images.velog.io/images/jsh5408/post/7bdc3f5c-de88-4033-9294-9f95602bc678/image.png)

#### 다른 사람의 풀이
```
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
```
stack 을 이용하면 작은 값들을 제거하기 편함

맨 처음 값을 `stack` 에 넣어주고 그 다음 숫자들부터 보면서 현재 숫자보다 작은 값들 제거
=> `stack` 의 가장 마지막 값과 현재 숫자를 비교

`k` 가 0 이 아니면 `k` 개 만큼 뒤 숫자들 제거

이렇게 간단하게 풀 수 있다니...

![](https://images.velog.io/images/jsh5408/post/e76488ba-f27e-4456-9c23-e651c9c3da2b/image.png)
