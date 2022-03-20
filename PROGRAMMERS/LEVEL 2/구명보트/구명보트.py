def solution(people, limit):
    answer = len(people)
    people.sort()
    idx = 0
    for i in range(len(people)-1, -1, -1):
        if people[i] == 0:
            continue
        for j in range(idx, i):
            if people[i] + people[j] <= limit:
                people[i] += people[j]
                people[j] = 0
                idx = j+1
            else:
                break
    zero = people.count(0)
    
    return answer - zero