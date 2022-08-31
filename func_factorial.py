def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)


num1, num2 = int(input()), int(input())
result = factorial(num1) / factorial(num2)
print(f'{result:.2f}')

#factirial is--- 5! = 5*4*3*2*1