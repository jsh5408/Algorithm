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