## 베스트앨범 - Level 3
https://programmers.co.kr/learn/courses/30/lessons/42579

#### 내 풀이 - 정확성: 6.7 | 합계: 6.7 / 100.0
```
import collections

def solution(genres, plays):
    total = collections.defaultdict(int)
    gp = collections.defaultdict(list)
    top2 = collections.defaultdict(list)
    
    for i in range(len(genres)):
        total[genres[i]] += plays[i]
        gp[genres[i]].append((plays[i], i))
    
    for k, v in gp.items():
        v.sort(reverse=True)
        top2[k] = v[:2]
    
    genres = set(genres)
    
    ans = []
    ansGenres = []
    for g in genres:
        if len(ansGenres) == 0:
            ansGenres.append(g)
        elif len(ansGenres) == 1:
            if total[ansGenres[0]] > total[g]:
                ansGenres += [g]
            else:
                ansGenres = [g] + ansGenres
        else:
            for i in range(2):
                if total[ansGenres[i]] < total[g]:
                    ansGenres = ansGenres[:i] + [g] + ansGenres[i:len(ansGenres)-1]
                    
    for g in ansGenres:
        ans += [top2[g][0][1], top2[g][1][1]]
    
    return ans
```
`total` 은 각 장르마다 재생횟수를 묶어줌
ex) `'classic': 1450`

`gp` 는 장르별 고유번호 재생횟수
ex) `'classic': [(500, 0), (150, 2), (800, 3)]`

`top2` 는 장르별 재생횟수 상위 2
ex) `'classic': [(800, 3), (500, 0)]`

1. `total`, `gp` 구하기

2. `gp` 기반으로 정렬하고 2개씩 잘라서 `top2` 구하기

3. 중복 없이 `genres` 들을 보면서 재생횟수가 가장 높은 2 가지의 장르 선별
=> 재생횟수 비교해서 순서 update

4. 두 장르의 `top2` 고유 번호만 `ans` 에 저장 후 return

#### 다른 사람 풀이 - 정확성: 100.0 | 합계: 100.0 / 100.0
```
def solution(genres, plays):
    answer = []
    
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
        
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
        
    return answer
```
`d` 에 우선 장르들만 key 값으로 저장

각 장르마다 (재생횟수, 고유번호) 묶어서 저장

`genreSort`: 장르별 전체 재생횟수를 기준으로 정렬
=> `x: sum(map(lambda y: y[0],d[x]))`

`genreSort` 의 장르들을 보면서 상위 2 개의 고유번호 추출
=> 장르별 (재생횟수, 고유번호) 들을 역순으로 정렬하고 2 개까지 slice
* `min(len(temp),2)` => "장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다." 처리