def print_1(n):
    a = 1
    for i in range(n):
        for j in range(n):
            print(a, end=" ")
            a +=1
            if a > 9:
                a = 1
        print()


row = int(input())

print_1(row)