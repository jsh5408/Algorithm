from sys import stdin

N = int(stdin.readline())

def hanoi(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi(n-1, start, 6-start-end)	# 1
    print(start, end)			# 2
    hanoi(n-1, 6-start-end, end)	# 3

print(2**N - 1)
hanoi(N, 1, 3)