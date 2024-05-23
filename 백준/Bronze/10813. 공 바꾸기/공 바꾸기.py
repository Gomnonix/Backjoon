n, m = map(int, input().split())
basket = list(map(int, range(1, n+1)))

temp = 0
for _ in range(m):
    i, j = map(int, input().split())

    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for i in basket:
    print(i, end=" ")
