a = int(input())
sum = 0
while a>=0:
    if a%5==0:
        sum += a//5
        print(sum)
        break
    a -= 3
    sum += 1

else:
    print(-1)
