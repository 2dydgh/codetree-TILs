def print_stars(n,m):
    for i in range(n):
        print("1"*m)

row, col = (map(int,input().split()))
print_stars(row,col)