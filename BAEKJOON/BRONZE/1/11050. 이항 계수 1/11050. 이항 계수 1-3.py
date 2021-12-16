from sys import stdin
from math import factorial

N, K = map(int, stdin.readline().split())

print(factorial(N) // (factorial(K) * factorial(N-K)))