## 카펫 - Level 2
https://programmers.co.kr/learn/courses/30/lessons/42842

#### 내 풀이 - 통과
```
def solution(brown, yellow):
    answer = []
    
    for i in range(yellow, 0, -1):
        w = i
        h = yellow // i + yellow % i
        b = w * 2 + h * 2 + 4 + (w*h - yellow)
        if b == brown:
            if w > h:
                return [w+2, h+2]
            else:
                return [h+2, w+2]
    
    return answer
```
`yellow` 의 형태가 어떨지 모르기 때문에 (항상 정사각형의 모양이란 보장이 X)
`yellow ~ 1` 까지의 모든 범위 확인

가로 `w` = `i`
세로 `h` = `yellow // i + yellow % i`
> `yellow // i` : ㅁ 모양처럼 모든 줄이 `i` 개만큼 꽉 참
`yellow % i` : ㄱ 모양처럼 일부가 비어있는 경우
>
를 합한 것이 세로가 됨

yellow 를 감싼 브라운의 개수 `b` = `w * 2 + h * 2 + 4 + (w*h - yellow)`
> `w * 2 + h * 2` : 순수 yellow 를 감싼 브라운
`4` : 4 개의 모서리
`(w*h - yellow)` : ㄱ 모양처럼 비어있는 곳을 채워주는 브라운

`if b == brown:` => 더 큰 값을 가로로 잡아서 return

![](https://images.velog.io/images/jsh5408/post/f4990f95-64ce-4364-a6c8-9f27d9d52fee/image.png)

#### 다른 사람의 풀이
```
def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]
```
이 문제는 역시 공식이 있었다..^^

`1 ~ 루트 yellow` 까지의 숫자들 중에 `yellow` 의 약수
그 중에서도 `if 2*(i + yellow//i) == brown-4:` 를 만족하는 `i` 찾기

![](https://images.velog.io/images/jsh5408/post/8c284769-340a-41c9-9e77-8f1276d24ac9/image.png)

확실히 더 빠르다^^