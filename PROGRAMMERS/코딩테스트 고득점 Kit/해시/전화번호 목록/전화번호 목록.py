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