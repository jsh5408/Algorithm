from sys import stdin
import collections

N = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

count = collections.Counter(cards)

for n in nums:
    print(count[n], end=" ")