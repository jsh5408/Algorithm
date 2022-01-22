n = int(input())

a = 0
b = 1
result = 0

for i in range(n+1):
    result += a
    a = b
    b = result

print(result)
