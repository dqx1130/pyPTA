def factorial(num):
    if num <= 1 :
        return 1
    return num * factorial(num-1)


n = eval(input())
print(factorial(abs(int(n))))
