def gong(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n, m = map(int,input().split())
result = gong(n, m)
print(result)