## N으로 표현
https://programmers.co.kr/learn/courses/30/lessons/42895

#### 다른 사람의 풀이
```
def solution(N, number):
    dp = [[]]

    x = 0
    for i in range(1, 9):
        dp.append(set())
        x = 10*x + N
        dp[i].add(x) # N, NN, NNN...

        for j in range(i):
            # 연산자 케이스 
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)


            if number in dp[i]:
                return i

    return -1
```
어떻게 해야할지 감도 안와서 다른 사람의 풀이부터 확인함

`1 ~ 9` 만큼의 `dp` 를 만들기
`i` 는 `N` 을 몇번 사용했는지를 의미한다

ex) `N = 5`
`dp[1]` 일 때 `x` = `5`, `dp[2]` 일 때 `x` = `55`, `dp[3]` 일 때 `x` = `555`, ...

다음은 연산자와 함께 사용하는 경우
예를 들어 `dp[2]` 일 때 그냥 숫자 `55` 도 있지만
`5+5`, `5-5`, `5*5`, `5//5` 사칙연산도 해당하므로
사칙연산의 경우들도 모두 add 해줌

모든 경우의 숫자들이 `dp` 에 저장되면 그 중에 `number` 를 찾아 return `i`

`N` 이 9 이하라서 가능한듯하다

![](https://images.velog.io/images/jsh5408/post/9d28c298-65c1-478b-83e7-0b9c7a938cb5/image.png)