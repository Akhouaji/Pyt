def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
x = int(input("Give a number "))
output = []
for i in range(x):
    output.append(fibonacci(i))

print(*output)