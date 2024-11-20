def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("Give a number! "))
print(f"The Factorial of {num} is {factorial(num)}")