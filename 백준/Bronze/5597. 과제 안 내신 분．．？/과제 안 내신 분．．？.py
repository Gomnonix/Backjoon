n = list(range(1, 31))

for _ in range(28):
    a = int(input())
    n.pop(n.index(a))

for i in n:
    print(i, end=" ")