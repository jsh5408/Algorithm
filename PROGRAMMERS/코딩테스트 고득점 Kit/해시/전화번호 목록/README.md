https://programmers.co.kr/learn/courses/30/lessons/42577

#### Brute Force - 실패
```
def solution(phone_book):
    answer = True
    
    phone_book.sort(key=len)
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                return False
    
    return answer
```
번호의 길이순으로 정렬하고 자신보다 더 긴 값들과 접두어를 비교
당연히 효율성 실패를 예상했다...

![](https://velog.velcdn.com/images/jsh5408/post/370ea9f3-43ab-4e47-88c6-2fa7c3ee433b/image.png)

#### Dictionary - 성공
```
def solution(phone_book):
    answer = True
    
    dic = {}
    phone_book.sort(key=len)
    for i in range(len(phone_book)):
        for j in range(len(phone_book[i])):
            if phone_book[i][:j+1] in dic:
                return False
        dic[phone_book[i]] = 1
    
    return answer
```
dic 를 만들어서 번호들을 저장하고 각 번호마다 접두사가 dic 에 포함됐는지 확인

![](https://velog.velcdn.com/images/jsh5408/post/462920cd-bb69-4e2f-8254-275bb45728be/image.png)

#### 그 외
* 미리 모든 번호로 dictionary 를 만들어두고 있는지 확인
* sort + startswith
```
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
```
간단하게 처리 가능
