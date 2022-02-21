def solution(phone_book):
    phone_book.sort(key=len)
    prefix = set()
    for p in phone_book:
        for i in range(1, len(p)):
            if p[:i] in prefix:
                return False
        prefix.add(p)
    
    return True