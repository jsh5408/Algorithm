## 위장 - Level 2
https://programmers.co.kr/learn/courses/30/lessons/42578

#### 내 풀이 - 정확성: 28.6 | 합계: 28.6 / 100.0
```
import collections

def solution(clothes):
    dic = collections.defaultdict(list)
    combinations = set()
    for c in clothes:
        dic[c[1]].append(c[0])
        combinations.add(c[0])
    
    types = list(dic.keys())
    
    def combination(types, comb):
        if comb:
            combinations.add(comb)
            
        if len(types) == 0:
            return
            
        for c in dic[types[0]]:
            combinations.add(c)
            combination(types[1:], comb+c)
    
    combination(types, "")
        
    return len(combinations)
```
우선 옷의 종류와 이름을 묶어주는 `dic` 생성
`combinations` 에는 옷의 이름들을 넣어주기 => set 로 중복 X

`types` 는 옷의 종류들만 저장

재귀 함수로 조합 찾기
모든 `comb` 조합들이 `combinations` 에 저장되면 최종적으로 길이 return

근데 안됨...

#### 다른 사람 풀이 - 정확성: 100.0 | 합계: 100.0 / 100.0
```
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1
```
조합을 직접 찾지 않아도 개수로 계산 가능

옷의 종류별로 개수를 세준다
1 개만 입는 경우도 있으니까 초기값은 2, 나머지는 1 씩 추가

다 구해줬으면 종류별 개수를 곱해줌 => `cnt`

모두 안입은 경우 한가지를 빼주고 return