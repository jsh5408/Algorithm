https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

#### Dictionary - 성공
```
def solution(s):
    answer = ''
    numDict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    tmp = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            tmp += s[i]
            
        if tmp in numDict:
            answer += numDict[tmp]
            tmp = ''
    if tmp:
        answer += tmp
            
    return int(answer)
```
`numDict` 에 0 ~ 9 까지의 숫자와 영단어 대응을 저장
`s` 를 한 char 씩 보면서 숫자면 `answer` 에 바로 추가
=> `isdigit()` 으로 숫자인지 판별
숫자가 아니라면 `tmp` 에 저장 + `tmp` 는 `numDict` 에 포함되는지 확인해서 치환
마지막에 return 할 때는 int 형으로 변환해서 반환했다.