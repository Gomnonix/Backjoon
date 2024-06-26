t = int(input())
arr = []
for _ in range(t):
    arr.append(list(map(int, input().split())))

for i in range(t):
    arr[i].sort(reverse=True)
    print(arr[i][2])