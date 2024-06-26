arr = []
arr2 = []
for i in range(3):
    p, y, s = input().split()
    arr.append(int(y))
    arr2.append([int(p), s])
arr.sort()
for i in arr:
    print(i%100, end="")
print()
arr2.sort(reverse=True)

for i in range(3):
    print(arr2[i][1][0], end="")