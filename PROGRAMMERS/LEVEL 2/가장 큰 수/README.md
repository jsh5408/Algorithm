## 가장 큰 수 - Level 2
https://programmers.co.kr/learn/courses/30/lessons/42746

#### 내 풀이 - 실패
```
def solution(numbers):
    answer = ''
    numbers.sort()
    dic = {i:[] for i in range(0, 10)}
    for i in range(len(numbers)):
        s = int(str(numbers[i])[0])
        if str(numbers[i])[-1] == "0":
            dic[s].insert(0, numbers[i])
        else:
            dic[s].append(numbers[i])
    
    for i in range(9, -1, -1):
        while dic[i]:
            answer += str(dic[i].pop())
    
    return answer
```
처음엔 재귀로 모든 조합들을 찾아서 max 값을 return 하려 했지만 타임리밋,,

그래서 큰 숫자들부터 앞자리에 배치하기로 했다.

우선 `numbers` 정렬 => sort()

`dic` 만들어서 `0 ~ 9` 의 숫자들 넣어줌

`numbers` 를 보면서 시작 값 `s` 에 해당하는 `dic[s]` 에 값 넣어주기
이 때, 0 으로 끝나는 숫자들은 insert 로 맨 앞에 넣어줌
ex) `[3, 30, 34, 5, 9]` => `dic[3] = [30, 3, 34]`, `dic[5] = [5]`, `dic[9] = [9]`

큰 숫자들부터 `answer` 에 붙여주고 return

그러나... 안됨!!
0 만 고려할게 아닌듯...

![](https://images.velog.io/images/jsh5408/post/70a0b2f5-7d8b-4695-87c9-0ec343538c61/image.png)

#### 다른 사람의 풀이
```
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
```
`numbers` 의 숫자들을 string 으로 변경
=> `list(map(str, numbers))` 알아두자!!

정렬은 "**`numbers` 값 * 3**" 기준 & 역순으로!!
3 을 곱해주는 이유는 **1,000 이하**의 숫자들이기 때문에 **세자리**로 맞추기 위해서
ex) `[3, 30, 34, 5, 9]` => `"9534330"`
int 형일 때, 그냥 sort() => `[34, 30, 9, 5, 3]` (❌)
str 형일 때, 그냥 sort() => `[9, 5, 34, 30, 3]` (❌)
str 형일 때, 3 곱한 값으로 sort() => `[999, 555, 343434, 333, 303030]` => `[9, 5, 34, 3, 30]` (⭕)

`000` 처럼 모든 숫자가 `0` 인 경우도 있으므로 int 로 변환했다가 다시 string 으로 변환

![](https://images.velog.io/images/jsh5408/post/aca7b673-67a8-473b-898c-c9542499842c/image.png)