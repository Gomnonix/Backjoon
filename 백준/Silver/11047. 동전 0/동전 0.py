n, k = map(int, input().split())
coin = []


for _ in range(n):
    a = int(input())
    coin.append(a)

coin.sort(reverse=True)
sum = 0
for i in coin:
    if k>0:
        sum += k//i
        k = k%i
    else:
        break

print(sum)
