import sys 
sys.setrecursionlimit(10**6)

def factorial(y):
    if y > 0:
        return y*factorial(y-1)
    else:
        return 1

def right_digit(n):
    if n[-1] == '0':
        return right_digit(n[:-1])
    else:
        return n[-1]
  

t = int(input())
for _ in range(t):
    y = int(input())
    n = str(factorial(y))
    result = right_digit(n)
    print(int(result))