while True:
    num = input()
    if num == "0":
        break
    yn = 1
    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            print("no")
            yn = 0
            break
    if yn:
        print("yes")