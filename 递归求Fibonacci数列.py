def f(n):
    if  n <= 2:
        return 1
    return f(n-1) + f(n-2)

for i in range(1,10):
    print(f(i))
