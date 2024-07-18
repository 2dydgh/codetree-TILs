n, m = map(int,input().split())
# result = gong(n, m)
# print(result)

for i in range(1, 10001):
     if (i % n == 0) and (i % m == 0):
        print(i)
        break